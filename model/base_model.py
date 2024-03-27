import time
from uuid import uuid4
from sqlalchemy import Column, DateTime, String, BigInteger
from datetime import datetime
from sqlalchemy import event

from constants import base_db


class BaseModel(base_db.Model):
    __abstract__ = True
    __table_args__ = {'mysql_charset': 'utf8mb4', 'mysql_engine': 'InnoDB'}
    id = Column(String(255), primary_key=True, nullable=False, comment="主键")
    create_time = Column(DateTime,  comment="创建时间")
    t = Column(BigInteger, comment="时间戳")


@event.listens_for(BaseModel, "before_insert", propagate=True)
def before_insert_listener(mapper, connection, model):
    model.id = uuid4()
    model.create_time = datetime.now()
    if model.t == None:
        model.t = time.time() * 1000


@event.listens_for(BaseModel, 'before_update', propagate=True)
def before_update_listener(mapper, connection, model):
    pass
