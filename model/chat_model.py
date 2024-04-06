from flask import g
from sqlalchemy import Column, BigInteger, Integer, String

from .base_model import BaseModel


class ChatModel(BaseModel):
    __tablename__ = "t_chat"

    title = Column(String(255), nullable=False, comment="标题")
    user_id = Column(String(255), nullable=False, comment="用户ID")
    type_code = Column(String(255), nullable=False, comment="专家类型")

    # 优点：能无限对话下去
    # 缺点: 遗忘上下文
    context_index = Column(Integer, nullable=False, default=0, comment="上下文开始索引")