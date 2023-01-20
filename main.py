from flask import Flask, render_template

from config import Config
from forms import MainForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/choose-your-destiny", methods=["POST", "GET"])
def choose_your_destiny():
    form = MainForm()
    if form.validate_on_submit():
        return render_template("game.html", form=form)
    else:
        return render_template("game.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
