from datetime import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.mircroblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            date = datetime.today()
            formatted_date = date.strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
            print(entry_content, formatted_date)

        get_entries = [(e["content"], e["date"], datetime.strptime(e["date"], "%Y-%m-%d").strftime("%b %d")) for e in app.db.entries.find({})]
        print(get_entries)
        return render_template("home.html", entries=get_entries)
    return app