from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


from controllers import database, day, user

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(day.bp)
app.register_blueprint(user.bp)

# TODO これ必要？
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("login.html")


if __name__ == "__main__":
    with app.app_context():
        database.init()
    app.run()
