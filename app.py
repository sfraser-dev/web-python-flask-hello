from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("first_page.html")

@app.route("/second/")
def hello_world_fancy():
    return render_template("second_page.html")

@app.route("/jinja2/")
def hello_world_jinja():
    return render_template(
        "jinja_intro.html",
        name="Homer Simpson",
        template_name="Jinja2")

# interpolation
color = "brown"
animal_one = "fox"
animal_two = "dog"

# addition and subraction
orange_amount = 2
apple_amount = 3
donate_amount = 15

# string concatenation
first_name = "Captain"
last_name = "Marvel"

# keyword args
kwargs = {
    "color": color,
    "animal_one": animal_one, 
    "animal_two": animal_two,
    "orange_amount": orange_amount,
    "apple_amount": apple_amount,
    "donate_amount" : donate_amount,
    "first_name" : first_name,
    "last_name" : last_name
} 

@app.route("/expressions/")
def hello_world_expressions():
    # use double star dictionary notation (passes key=value)
    return render_template("expressions.html", **kwargs)