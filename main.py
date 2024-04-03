import time
import jwt
from flask import Flask, g, request
from common import Result
from controller import chat_controller, context_controller, type_controller, user_controller
from constants import HOST, PORT, DEBUG, UID, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO, STATIC_FOLDER, base_db
from constants import ROUTE_WHITE_LIST, JWT_HEADER, JWT_SALT
from model import TypeModel
from prompts import prompts
from utils import PathUtil
from flask_cors import CORS

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
    for prompt in prompts:
        model = TypeModel(code=prompt.code, name=prompt.name, user_id=UID,
                          system_prompt=prompt.system_prompt, context_length=prompt.context_length, question_prompt=prompt.question_prompt, t=(time.time() * 1000 + count))
        base_db.session.add(model)
        count = count + 1
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

app.register_blueprint(user_controller)
app.register_blueprint(chat_controller)
app.register_blueprint(context_controller)
app.register_blueprint(type_controller)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
