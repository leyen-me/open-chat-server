from datetime import datetime, timedelta
from flask import Blueprint as Controller, request, g
import jwt
from constants import base_db
from model import UserModel
from common import Result
from constants import JWT_HEADER, JWT_SALT

user_controller = Controller("user", __name__, url_prefix='/user')


@user_controller.route("/login", methods=["POST"])
def login():
    email = request.json["email"]

    id = None
    db_user = base_db.session.query(UserModel).filter(
        UserModel.email == email).one_or_none()
    if not db_user:
        new_user = UserModel(email=email)
        base_db.session.add(new_user)
        base_db.session.commit()
        id = new_user.id
    else:
        id = db_user.id

    jwt_exp = datetime.now() + timedelta(hours=12)
    payload = {"exp": jwt_exp, "uid": id}
    token = jwt.encode(payload=payload, key=JWT_SALT,
                       algorithm=JWT_HEADER["alg"], headers=JWT_HEADER)
    return Result.ok(data=token)


@user_controller.route("/info", methods=["GET"])
def info():
    return Result.ok(data=g.uid)
