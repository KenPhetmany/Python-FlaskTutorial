import _datetime
import re
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, dfdf!"


@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=_datetime.date.today()
    )
