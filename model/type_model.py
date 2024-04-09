from flask import g
from sqlalchemy import Column, BigInteger, Integer, String, Text

from .base_model import BaseModel


class TypeModel(BaseModel):
    __tablename__ = "t_type"

    user_id = Column(String(255), nullable=False, comment="这个GPT属于谁")
    name = Column(String(255), nullable=False, comment="模型名称")
    code = Column(String(255), nullable=False, comment="agent name")

    def json(self):
        return {
            "id": self.id,
            "create_time": self.create_time.strftime("%Y-%m-%d"),
            "t": self.t,

            "user_id": self.user_id,
            "name": self.name,
            "code": self.code,
        }
