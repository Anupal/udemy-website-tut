from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("first_page.html", name="Anupal Mishra", website_name="Flask Tutorial")

@app.route("/fancy/")
def hello_world_fancy():
    return """
    <html>
    <h1>Greetings!</h1>
    <p>Hello, World!</p>
    </html>
    """