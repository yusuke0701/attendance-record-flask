from flask import Blueprint, render_template
from flask_login import login_required

from controllers.database import db_session
from models.user import User

bp = Blueprint("admin", __name__)


@login_required
@bp.route("/admin")
def index():
    users = db_session.query(User).all()
    for user in users:
        print(user.name)
    return render_template("admin.html", users=users)
