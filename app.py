from flask import Flask, render_template

app = Flask(__name__)

# first endpoint
@app.route("/")
def hello_world():
    return render_template("first_page.html")

# second endpoint
@app.route("/second/")
def hello_world_fancy():
    return render_template("second_page.html")

# third endpoint
@app.route("/jinja2/")
def hello_world_jinja():
    return render_template(
        "jinja_intro.html",
        name="Homer Simpson",
        template_name="Jinja2")

# variables
color = "brown"
animal_one = "fox"
animal_two = "dog"
orange_amount = 30
apple_amount = 20
donate_amount = 15
first_name = "Captain"
last_name = "Marvel"

# keyword args
kwargs_expressions = {
    "color": color,
    "animal_one": animal_one, 
    "animal_two": animal_two,
    "orange_amount": orange_amount,
    "apple_amount": apple_amount,
    "donate_amount" : donate_amount,
    "first_name" : first_name,
    "last_name" : last_name,
} 

# fourth endpoint
@app.route("/expressions/")
def hello_world_expressions():
    # use double star dictionary notation (passes key=value)
    return render_template("expressions.html", **kwargs_expressions)

# data collections / data structures
movies = ["Star Wars", "Ghostbusters", "Aliens"]
car = {"brand": "Ford", "model": "Mustang", "year": "2020"}
class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

kwargs_data_structures = {
    "movies" : movies,
    "car" : car,
    "moons" : moons
}

# fifth endpoint
@app.route("/data_structures/")
def hello_world_data_structures():
    return render_template(
        "data_structures.html", **kwargs_data_structures)

company = "Apple"     # "Apple" or "Microsoft"
# sixth endpoint
@app.route("/conditionals_if/")
def hello_world_conditionals_if():
    return render_template("conditionals_if.html", company = company)

planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_dict = {1:"Mercury", 2:"Venus", 3:"Earth", 4:"Mars", 5:"Jupiter", 6:"Saturn", 7:"Uranus", 8:"Neptune"}
# seventh endpoint
@app.route("/for_loop/")
def hello_world_for_loop():
    return render_template("for_loop.html",
                           planets_list = planets_list,
                           planets_dict = planets_dict)

user_os = {"William":"Windows", "Maria":"MacOS", "Laura":"Linux"}
# eighth endpoint
@app.route("/loops_and_conditionals/")
def hello_world_loops_and_conditionals():
    return render_template("loops_and_conditionals.html", user_os = user_os)