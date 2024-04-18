from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controllers import database, day, user
from models.user import User as models_User

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(day.bp)
app.register_blueprint(user.bp)

db_engine = create_engine("sqlite:///instance/db.sqlite", echo=True)
db_session = sessionmaker(db_engine)()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(models_User).filter(models_User.id == user_id).first()


@login_manager.unauthorized_handler
def unatuhorized_handler():
    return "ログインが必須のページです"


@app.route("/")
def index():
    return render_template("login.html")


if __name__ == "__main__":
    with app.app_context():
        database.init()
    app.run()
