from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.common import Base

db_engine = create_engine("sqlite:///instance/db.sqlite", echo=True)
db_session = sessionmaker(db_engine)()


def init():
    Base.metadata.create_all(db_session)
