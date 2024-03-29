from sqlalchemy import Column, BigInteger, Integer, String

from .base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = "t_user"

    email = Column(String(255), nullable=True, comment="邮箱")