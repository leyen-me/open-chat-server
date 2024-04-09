from enum import Enum
from .base_client import base_client as base_client
from .base_client import BASE_MODEL as BASE_MODEL
from .base_db import base_db as base_db


HOST = "0.0.0.0"

PORT = 8080

DEBUG = True

UID = "10001"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pdBGKGjRyX3Jb2Hn@localhost:3306/chat-openai-mysql?charset=utf8mb4"

SQLALCHEMY_ECHO = True

STATIC_FOLDER = "static"

ROUTE_WHITE_LIST = ["/user/login", "/static/**", "/image/**"]

JWT_HEADER = {
    "alg": "HS256",
    "typ": "JWT"
}

JWT_SALT = "asgfdgerhersasdq"

class CHAT_ROLES(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    PLUGIN = "assistant"
    FUNCTION = "function"

class CHAT_TYPE(Enum):
    # 正常聊天
    NORMAL = "NORMAL"

    # 总结
    RESUME = "RESUME"
