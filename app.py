from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


from controllers import database, day

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = b"abcdefghijklmn"  # FIXME Flaskのセッションを使うために必要。envファイル等に格納する

app.register_blueprint(day.bp)

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("start.html")


if __name__ == "__main__":
    with app.app_context():
        database.init()
    app.run()
