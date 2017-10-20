
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, Column, ForeignKey, String

app = Flask(__name__)

durations = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", durations=SongTime.query.all())

    color = float(request.form["color"])
    emotion = int(request.form["emotion"])
    filename = "/home/DennisDemenis/WebPage/stroop.txt"
    file = open(filename, 'a')
    file.write("\n");file.write(str(color)); file.write("\t");file.write(str(emotion));
    file.close()
    return redirect(url_for('index'))
