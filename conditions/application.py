import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    apr = now.month == 4 and now.day == 24
    return render_template("index.html", apr=apr)
