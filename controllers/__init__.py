# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config.from_object("config")

# from sqlalchemy import create_engine

# engine = create_engine(
#     "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type}"
# )

# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker

# SessionClass = sessionmaker(engine)
# session = SessionClass()
