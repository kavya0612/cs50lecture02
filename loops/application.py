from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Python", "Flask", "Jinja2"]
    return render_template("index.html", names=names)
