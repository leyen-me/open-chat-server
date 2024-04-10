import time
import contextlib
from io import StringIO
import os
import re
import sys
import subprocess
from uuid import uuid4
from flask import Blueprint as Controller, Response, make_response, request, g, send_file, stream_with_context
from constants import base_db, CHAT_TYPE
from model import ChatModel, ContextModel, TypeModel
from common import Result, AGENT_REGISTRY
from utils import FileUtil
from agents import *


chat_controller = Controller("chat", __name__, url_prefix='/chat')


@chat_controller.route("/", methods=["POST"])
def save_():
    title = request.json["title"]
    type_code = request.json["type_code"]
    model = ChatModel(title=title, user_id=g.uid, type_code=type_code)
    base_db.session.add(model)
    base_db.session.commit()
    return Result.ok(model.id)


@chat_controller.route("/<string:id>", methods=["DELETE"])
def delete_(id):
    base_db.session.query(ContextModel).filter(
        ContextModel.chat_id == id).delete()
    base_db.session.query(ChatModel).filter(ChatModel.id == id).delete()
    base_db.session.commit()
    return Result.ok()


@chat_controller.route("/all", methods=["DELETE"])
def delete_all_():
    ids = [chat.id for chat in base_db.session.query(
        ChatModel).filter(ChatModel.user_id == g.uid).all()]
    base_db.session.query(ChatModel).filter(
        ChatModel.user_id == g.uid).delete()
    base_db.session.query(ContextModel).filter(
        ContextModel.chat_id.in_(ids)).delete()
    base_db.session.commit()
    return Result.ok()


@chat_controller.route("/", methods=["PUT"])
def update_():
    vo = request.json
    model = base_db.session.query(ChatModel).filter(
        ChatModel.id == vo['id']).one()
    for key, value in vo.items():
        setattr(model, key, value)
    base_db.session.commit()
    return Result.ok()


@chat_controller.route("/<string:id>", methods=["GET"])
def info_(id):
    db_data = base_db.session.query(ChatModel).filter(ChatModel.id == id).one()
    return Result.ok({
        "id": db_data.id,
        "title": db_data.title,
        "user_id": db_data.user_id,
        "type_code": db_data.type_code,
        "create_time": str(db_data.create_time),
    })


@chat_controller.route("/list", methods=["GET"])
def chat_list_():
    db_data = base_db.session.query(ChatModel).filter(
        ChatModel.user_id == g.uid).order_by(ChatModel.t.desc()).all()
    data = []
    for item in db_data:
        data.append({
            "id": item.id,
            "title": item.title,
            "user_id": item.user_id,
            "type_code": item.type_code,
            "create_time": str(item.create_time),
        })
    return Result.ok(data)


def get_context(chat_id):
    """
    聊天时:获取上下文
    """
    messages = []
    context_list = base_db.session.query(ContextModel).filter(
        ContextModel.chat_id == chat_id, ContextModel.status == 1).order_by(ContextModel.t.asc()).all()
    for item in context_list:
        messages.append({
            "role": item.role,
            "content": item.content,
        })
    return messages


def save_question(chat_id, question):
    """
    保存问题
    """
    if question != "":
        user_context = ContextModel(
            chat_id=chat_id, content=question, role="user", status=1, tool_name=None, tool_parameters=None)
        base_db.session.add(user_context)
        base_db.session.commit()


def save_anwser(chat_id, anwser, execution_time):
    """
    保存回答
    """
    if anwser != "":
        assistant_context = ContextModel(
            chat_id=chat_id, content=anwser, role="assistant", status=1, tool_name="", tool_parameters=None, execution_time=execution_time)
        base_db.session.add(assistant_context)
        base_db.session.commit()


@chat_controller.route("/resume", methods=["POST"])
def resume_():
    chat_id = request.json["chat_id"]
    messages = get_context(chat_id)
    agent = ResumeAgent()
    for responses in agent.run(messages=messages):
        pass
    model = base_db.session.query(ChatModel).filter(
        ChatModel.id == chat_id).one()
    title = messages[-1].get('content', '')
    model.title = title.replace('"', '')
    base_db.session.commit()
    return Result.ok()


def code_run(code):
    """
    运行代码
    """
    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    with stdoutIO() as s:
        try:
            import matplotlib
            matplotlib.use('agg')
            exec(code)
        except Exception as e:
            return "代码运行失败:" + str(e)
    return "代码运行结果如下:" + s.getvalue()


@chat_controller.route("/code/auto/run/<string:chat_id>", methods=["POST"])
def code_auto_run_(chat_id):
    """
    Python自动运行代码
    """
    messages = get_context(chat_id, CHAT_TYPE.NORMAL)
    if len(messages) <= 0:
        return Result.ok()
    message = messages[-1]
    if message['role'] == "user":
        return Result.ok()

    pattern = r'```python(.*?)```'
    matched_code = re.findall(pattern, message['content'], re.DOTALL)
    for code in matched_code:
        res = code_run(code)
        assistant_context = ContextModel(
            chat_id=chat_id, content=res, role="assistant", status=1, tool_name="", tool_parameters=None)
        base_db.session.add(assistant_context)
        base_db.session.commit()

    return Result.ok()


@chat_controller.route("/code/pkg", methods=["POST"])
def code_pkg_():
    """
    打包代码
    """
    code = request.json["code"]

    def generate():
        import platform
        file_name = str(uuid4())
        spec_path = os.path.join(os.getcwd(), file_name + ".spec")
        build_path = os.path.join(os.getcwd(), "build", file_name)
        file_path = os.path.join(os.getcwd(), "dist", file_name + ".py")
        zip_path = os.path.join(os.getcwd(), "dist", file_name + ".zip")
        if platform.system() == 'Linux':
            exe_path = os.path.join(os.getcwd(), "dist", file_name)
        elif platform.system() == 'Windows':
            exe_path = os.path.join(os.getcwd(), "dist", file_name + ".exe")

        with open(file_path, 'w+', encoding='utf-8') as file:
            file.write(code + "\n" + 'input("按任意键退出...")')

        yield "正在生成二进制安装包..."
        # 生成二进制安装包
        subprocess.run(
            ['pyinstaller', '-F', file_path], check=True, shell=True, encoding='utf-8')

        yield "压缩中..."
        FileUtil.zip(exe_path, zip_path)

        yield "清除缓存"
        # 删除源代码
        FileUtil.delete_file(file_path)
        # 删除安装包
        FileUtil.delete_file(exe_path)
        # 删除spec
        FileUtil.delete_file(spec_path)
        # 删除构建缓存目录
        FileUtil.delete_dir(build_path)

        yield "文件生成成功:" + file_name

    return Response(stream_with_context(generate()))


@chat_controller.route("/code/pkg/download/", methods=["POST"])
def code_pkg_download_():
    file_name = request.json["file_name"]
    file_path = os.path.join(os.getcwd(), "dist", file_name + ".zip")
    response = make_response(send_file(file_path, as_attachment=True))
    response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
    return response


def get_stream_response(chat_id):
    messages = []
    db_chat = base_db.session.query(ChatModel).filter(
        ChatModel.id == chat_id).one()
    db_type = base_db.session.query(TypeModel).filter(
        TypeModel.code == db_chat.type_code).one()
    context_list = base_db.session.query(ContextModel).filter(
        ContextModel.chat_id == chat_id, ContextModel.status == 1).order_by(ContextModel.t.asc()).all()

    for item in context_list:
        messages.append({
            "role": item.role,
            "content": item.content,
        })

    start_time = time.perf_counter()

    def generate():
        agent = AGENT_REGISTRY[db_type.code]()

        old_message = ""
        for responses in agent.run(messages=messages):
            show_message = responses[-1]["content"].replace(old_message, "")
            yield show_message
            old_message = responses[-1]["content"]

        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000

        count = 0
        for response in responses:
            function_call = response.get('function_call', None)
            tool_name = None
            tool_parameters = None
            content = response["content"].replace(
                "http://127.0.0.1:7865/static/", "http://127.0.0.1:8080/image/")
            if function_call:
                tool_name = function_call.get('name', None)
                tool_parameters = function_call.get('arguments', None)

            model = ContextModel(
                chat_id=chat_id, content=content, role=response["role"], status=1, tool_name=tool_name, tool_parameters=tool_parameters, execution_time=execution_time, t=(time.time() * 1000 + count))
            base_db.session.add(model)
            count += 1

        base_db.session.commit()

    return Response(stream_with_context(generate()))


@chat_controller.route("/stream", methods=["POST"])
def stream_():
    """
    聊天
    """
    chat_id = request.json["chat_id"]
    question = request.json["question"]

    # 保存用户提问
    save_question(chat_id, question)
    return get_stream_response(chat_id)


@chat_controller.route("/re/stream", methods=["POST"])
def re_stream_():
    """
    重试
    """
    chat_id = request.json["chat_id"]

    # 删除最后
    context_list = base_db.session.query(ContextModel).filter(
        ContextModel.chat_id == chat_id, ContextModel.status == 1).order_by(ContextModel.t.asc()).all()

    if len(context_list) > 0:
        last_context = context_list[-1]
        if last_context.role == "assistant":
            base_db.session.delete(last_context)
            base_db.session.commit()

    return get_stream_response(chat_id)
