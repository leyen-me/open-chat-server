from flask import g
from sqlalchemy import Column, BigInteger, Integer, String

from .base_model import BaseModel


class TypeModel(BaseModel):
    __tablename__ = "t_type"
    
    code = Column(String(255), nullable=False, comment="模型编码")
    user_id = Column(String(255), nullable=False, comment="这个GPT属于谁")
    name = Column(String(255), nullable=False, comment="模型名称")
    system_prompt = Column(String(1000), nullable=False, comment="系统提示词")