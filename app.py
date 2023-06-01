from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("first_page.html")

@app.route("/second")
def hello_world_fancy():
    return render_template("second_page.html")

@app.route("/jinja2")
def hello_world_jinja():
    return render_template(
        "jinja_intro.html",
        name="Homer Simpson",
        template_name="Jinja2")