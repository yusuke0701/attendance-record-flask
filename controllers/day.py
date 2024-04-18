from datetime import datetime

from flask import Blueprint, session as flask_session, render_template
from flask_login import login_required, current_user

from controllers.database import db_session
from models.day import Day

bp = Blueprint("day", __name__)


@bp.route("/start", methods=["POST"])
@login_required
def start():
    new_day = Day(user_id=current_user.id)

    db_session.add(new_day)
    db_session.commit()

    flask_session["day_id"] = new_day.id

    return render_template("end.html")


@bp.route("/end", methods=["POST"])
@login_required
def end():
    day = db_session.get(Day, flask_session["day_id"])
    if day is None:
        return "Internal Server Error"

    day.check_out = datetime.now()
    day.working_seconds = day.check_out - day.check_in

    db_session.commit()

    flask_session["day_id"] = -1

    return render_template("start.html")
