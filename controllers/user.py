from flask import Blueprint, request, render_template
from flask_login import login_user, logout_user

import controllers.admin
from controllers.database import db_session
from models.user import User, UserClass

bp = Blueprint("user", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    if not all([email, password]):
        return "Bad Request"

    user = db_session.query(User).filter(User.email == email).first()
    if user is None:
        return "登録されていないEmailアドレスです。"
    if str(user.password) != password:
        return "パスワードが間違っています。"

    login_user(user, remember=True)

    # 管理者は専用ページへ遷移
    if UserClass(user.user_class) == UserClass.Admin:
        return controllers.admin.index()

    return render_template("start.html")


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return render_template("login.html")


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
