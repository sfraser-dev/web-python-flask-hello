from flask import Flask, render_template

# app factory pattern
def create_app():
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

    # fourth endpoint, expressions example
    @app.route("/expressions/")
    def hello_world_expressions():
        return render_template("expressions.html", **{
            "color": "brown",
            "animal_one": "fox",
            "animal_two": "dog",
            "orange_amount": 30,
            "apple_amount": 20,
            "donate_amount": 15,
            "first_name": "Captain",
            "last_name": "Marvel",
        })

    # fifth endpoint, data structures example
    @app.route("/data_structures/")
    def hello_world_data_structures():
        movies = ["Star Wars", "Ghostbusters", "Aliens"]
        car = {"brand": "Ford", "model": "Mustang", "year": "2020"}
        class GalileanMoons:
            def __init__(self, first, second, third, fourth):
                self.first = first
                self.second = second
                self.third = third
                self.fourth = fourth
        moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
        return render_template("data_structures.html", movies=movies, car=car, moons=moons)

    # sixth endpoint
    @app.route("/conditionals_if/")
    def hello_world_conditionals_if():
        return render_template("conditionals_if.html", company="Apple")

    # seventh endpoint
    @app.route("/for_loop/")
    def hello_world_for_loop():
        planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        planets_dict = {1:"Mercury", 2:"Venus", 3:"Earth", 4:"Mars", 5:"Jupiter", 6:"Saturn", 7:"Uranus", 8:"Neptune"}
        return render_template("for_loop.html", planets_list=planets_list, planets_dict=planets_dict)

    # eighth endpoint
    @app.route("/loops_and_conditionals/")
    def hello_world_loops_and_conditionals():
        user_os = {"William":"Windows", "Maria":"MacOS", "Laura":"Linux"}
        return render_template("loops_and_conditionals.html", user_os=user_os)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)