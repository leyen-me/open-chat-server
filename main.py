import io
import os
import time
import jwt
from flask import Flask, g, request, send_file
from common import Result
from controller import chat_controller, context_controller, type_controller, user_controller
from constants import HOST, PORT, DEBUG, UID, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO, STATIC_FOLDER, base_db
from constants import ROUTE_WHITE_LIST, JWT_HEADER, JWT_SALT
from model import TypeModel
from utils import PathUtil
from flask_cors import CORS
from agents import *

app = Flask(__name__, static_folder=STATIC_FOLDER)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO

CORS(app)
base_db.init_app(app)

with app.app_context():
    # 创建表
    base_db.create_all()

    base_db.session.query(TypeModel).delete()
    base_db.session.commit()

    count = 0
    model = TypeModel(code=ChatAgent.name, name="仅聊天",
                      user_id=UID, t=(time.time() * 1000 + count))
    base_db.session.add(model)

    count = count + 1
    model = TypeModel(code=CommonAgent.name, name="通用",
                      user_id=UID, t=(time.time() * 1000 + count))
    base_db.session.add(model)

    count = count + 1
    model = TypeModel(code=IotAgent.name, name="IoT",
                      user_id=UID, t=(time.time() * 1000 + count))
    base_db.session.add(model)
    
    count = count + 1
    model = TypeModel(code=CompileTeacherAgent.name, name="编译原理老师",
                      user_id=UID, t=(time.time() * 1000 + count))
    base_db.session.add(model)

    base_db.session.commit()


@app.before_request
def before():
    # 跳过OPTIONS请求
    if request.method == 'OPTIONS':
        return
    if PathUtil.is_path_allowed(request.path, ROUTE_WHITE_LIST):
        return

    authorization = request.headers.get("Authorization")
    if authorization is None:
        return Result.logout()
    else:
        # 校验JWT
        try:
            info = jwt.decode(authorization, JWT_SALT, verify=True,
                              algorithms=JWT_HEADER["alg"])
        except Exception as e:
            return Result.logout()
        # 校验数据库
        g.uid = info["uid"]


@app.errorhandler(Exception)
def exception(error_msg):
    return Result.error(str(error_msg))


@app.route('/image/<string:id>')
def send_image(id):
    img_path = os.path.join(os.getcwd(), "workspace", "ci_workspace", id)
    response = send_file(img_path, mimetype='image/jpeg', as_attachment=True)
    response.headers['Content-Disposition'] = 'inline; filename="image.jpg"'
    return response


app.register_blueprint(user_controller)
app.register_blueprint(chat_controller)
app.register_blueprint(context_controller)
app.register_blueprint(type_controller)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
