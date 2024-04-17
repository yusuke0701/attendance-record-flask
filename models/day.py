from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Interval

from models.common import Base


class Day(Base):
    """
    Day はユーザーが打刻したデータです。
    """

    __tablename__ = "day"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)  # TODO 外部キー制約
    check_in = Column(DateTime, nullable=False, default=datetime.now())
    check_out = Column(DateTime)
    edited_check_in = Column(DateTime)
    edited_check_out = Column(DateTime)
    working_seconds = Column(Interval)
