from datetime import datetime

from flask import Blueprint, render_template, session

from controllers.database import db_session
from models.day import Day

bp = Blueprint("day", __name__)


@bp.route("/start", methods=["POST"])
def start():
    new_day = Day()

    db_session.add(new_day)
    db_session.commit()

    session["day_id"] = new_day.id

    return render_template("end.html")


@bp.route("/end", methods=["POST"])
def end():
    day = db_session.get(Day, flask_session["day_id"])
    if day is None:
        return "Internal Server Error"

    day.check_out = datetime.now()

    db_session.commit()

    session["day_id"] = -1

    return render_template("start.html")
