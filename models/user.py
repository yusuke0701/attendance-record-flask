import enum

from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Enum

from models.common import Base


class UserClass(enum.Enum):
    """
    UserClass は各ユーザーのシステム上での扱いを示します。
    """

    General = 1  # 一般社員
    Superior = 2  # 上長
    Admin = 3  # システム管理者


class User(Base, UserMixin):
    """
    User は各ユーザーのデータです。
    ログインに使用します。
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    user_class = Column(Enum(UserClass), nullable=False, default=UserClass.General)
    superior_id = Column(Integer)
