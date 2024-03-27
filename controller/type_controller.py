from flask import Blueprint as Controller
from model import TypeModel
from common import Result
from constants import base_db


type_controller = Controller("type", __name__, url_prefix='/type')


@type_controller.route("/list", methods=["GET"])
def list_():
    db_data = base_db.session.query(
        TypeModel).order_by(TypeModel.t.asc()).all()
    data = []
    for item in db_data:
        data.append(item.json())
    return Result.ok(data)
