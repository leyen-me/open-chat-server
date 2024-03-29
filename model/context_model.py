from flask import g
from sqlalchemy import Column, BigInteger, Integer, String, Text, UnicodeText

from .base_model import BaseModel


class ContextModel(BaseModel):
    __tablename__ = "t_context"
    
    chat_id = Column(String(255), nullable=False, comment="聊天ID")
    content = Column(Text, comment="内容")
    role = Column(String(20), nullable=False, comment="角色")
    status = Column(Integer, nullable=False, comment="状态")
    tool_name = Column(String(255), comment="工具名称")
    tool_parameters = Column(Text, comment="工具参数")

    def json(self):
        return {
            "id": self.id,
            "create_time": str(self.create_time),

            "chat_id": self.chat_id,
            "content": self.content,
            "role": self.role,
            "status": self.status,
            "tool_name": self.tool_name,
            "tool_parameters": self.tool_parameters,
            "t": self.t,
        }