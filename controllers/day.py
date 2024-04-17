from datetime import datetime

from flask import Blueprint, render_template, session

from controllers.database import Session
from models.day import Day

bp = Blueprint("day", __name__)


@bp.route("/start", methods=["POST"])
def start():
    new_day = Day()

    Session.add(new_day)
    Session.commit()

    session["day_id"] = new_day.id

    return render_template("end.html")


@bp.route("/end", methods=["POST"])
def end():
    day = Session.get(Day, session["day_id"])
    day.check_out = datetime.now()

    Session.commit()

    session["day_id"] = -1

    return render_template("start.html")
