from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Date, Interval

from models.common import Base


class Month(Base):
    """
    Month は打刻データを月毎にまとめたデータです。
    """

    __tablename__ = "month"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)  # TODO 外部キー制約
    year_month = Column(Date, nullable=False)
    working_seconds = Column(Interval, nullable=False)
