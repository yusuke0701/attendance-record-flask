from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.common import Base

e = create_engine("sqlite:///instance/db.sqlite", echo=True)
s = sessionmaker(e)

Session = s()


def init():
    Base.metadata.create_all(e)
