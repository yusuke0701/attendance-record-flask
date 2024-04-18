from flask import Blueprint, request, render_template

from controllers.database import db_session
from models.user import User

bp = Blueprint("user", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    user = db_session.query(User).filter(User.email == email).first()
    if user is None:
        return "登録されていないEmailアドレスです。"
    if str(user.password) != password:
        return "パスワードが間違っています。"

    return render_template("start.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = User(name=name, email=email, password=password)

    db_session.add(new_user)
    db_session.commit()

    return render_template("login.html")
