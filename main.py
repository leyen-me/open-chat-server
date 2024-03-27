from flask import Flask, g
from common import Result
from controller import chat_controller, context_controller, type_controller
from constants import HOST, PORT, DEBUG, UID, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO, STATIC_FOLDER, base_db
from constants import CHAT_SYSTEM_PROMPT, TRANSLATE_SYSTEM_PROMPT, MATPLOTLIB_SYSTEM_PROMPT
from model import TypeModel

app = Flask(__name__, static_folder=STATIC_FOLDER)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO


def db_init(app):
    base_db.init_app(app)

    with app.app_context():
        # 创建表
        base_db.create_all()

        # 通用
        default_model = base_db.session.query(TypeModel).filter(
            TypeModel.code == "default").one_or_none()
        if not default_model:
            default_model = TypeModel(code="default", name="通用", user_id=UID,
                                      system_prompt=CHAT_SYSTEM_PROMPT)
            base_db.session.add(default_model)
            base_db.session.commit()

        # 翻译
        translate_model = base_db.session.query(TypeModel).filter(
            TypeModel.code == "translate").one_or_none()
        if not translate_model:
            translate_model = TypeModel(code="translate", name="翻译", user_id=UID,
                                        system_prompt=TRANSLATE_SYSTEM_PROMPT)
            base_db.session.add(translate_model)
            base_db.session.commit()

        # 翻译
        matplotlib_model = base_db.session.query(TypeModel).filter(
            TypeModel.code == "matplotlib").one_or_none()
        if not matplotlib_model:
            matplotlib_model = TypeModel(code="matplotlib", name="数据分析", user_id=UID,
                                         system_prompt=MATPLOTLIB_SYSTEM_PROMPT)
            base_db.session.add(matplotlib_model)
            base_db.session.commit()


db_init(app)


@app.before_request
def before():
    g.uid = UID


@app.errorhandler(Exception)
def exception(error_msg):
    return Result.error(str(error_msg))


app.register_blueprint(chat_controller)
app.register_blueprint(context_controller)
app.register_blueprint(type_controller)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
