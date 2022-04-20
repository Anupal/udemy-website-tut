from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return_template("index.html", title="Habit Tracker - Home")

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    return render_template("add_habit.html", title="Habbit Tracker - Add Habit")