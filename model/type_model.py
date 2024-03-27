from flask import g
from sqlalchemy import Column, BigInteger, Integer, String

from .base_model import BaseModel


class TypeModel(BaseModel):
    __tablename__ = "t_type"

    code = Column(String(255), nullable=False, comment="模型编码")
    user_id = Column(String(255), nullable=False, comment="这个GPT属于谁")
    name = Column(String(255), nullable=False, comment="模型名称")
    system_prompt = Column(String(1000), nullable=False, comment="系统提示词")
    code_auto_run = Column(Integer, nullable=False,
                           default=0, comment="代码是否自动运行")

    def json(self):
        return {
            "id": self.id,
            "create_time": self.create_time.strftime("%Y-%m-%d"),
            "t": self.t,

            "code": self.code,
            "user_id": self.user_id,
            "name": self.name,
            "system_prompt": self.system_prompt,
            "code_auto_run": self.code_auto_run,
        }
