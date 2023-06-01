General Flask information:
Micro framework, doesn't do much, allows us to receive user data and send
data back as per user requests. Because it doesn't do that much for us, we
can write our applications in pure python, it doesn't tell us how we should
be writing our code.

# Installing flask on windows / powershell terminal (within vscode)
(1) Install python 3

(2) Create a virtual environment (pyenv) Pyenv for windows: https://github.com/pyenv-win/pyenv-win

    # Powershell install:
    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
    # restart Powershell
    pyenv --version
    
    # How to use pyenv (same commands apply to pyenv for windows)
    # https://blog.teclado.com/how-to-use-pyenv-manage-python-versions/
    
    # Teclado microblog code uses python 3.9.0
    pyenv install --list
    pyenv versions
    pyenv install 3.9.0
    pyenv versions
    pyenv local 3.9.0
    pyenv local
    # create a virtual environment (intellisence can now work)
    pyenv exec python -m venv .venv
    # activate the virtual environment
    .\.venv\Scripts\activate

(3) Install Flask
    pip install Flask

(4) Write Flask app in file app.py (default for Flask)

    from flask import Flask
    app = Flask(__name__)
    @app.route("/")
    def hello_world():
        return "Hello, world!"

(5) Set flask environment variables (powershell)
    # Tell Flask before we run it which python file contains the Flask app
    $env:FLASK_APP = "app.py"
    $env:FLASK_APP
    $env:FLASK_DEBUG = 1
    $env:FLASK_DEBUG

(6) Now we can run flask
    flask run

####################
Content that is static doesn't have to be generated, modified or processed.
The server just delivers the file to the user and the user uses it, it doesn't
have to go through any processing by the user.

In flask, HTML files go into a folder called "templates/" and this folder should
be in the same directory as the "app.py" file. The directory should be the the
top dir of the project - this is what Flask expects and looks for. For example,
"first_page.html" and  "second_page.html" can go in "templates/".

Also need to import "render_template" in app.py as this allows naming a file to
be sent to the user.

In "app.py", the function names are largely irrelevant. What the user interacts with
are the endpoints (@app.route("/"), etc). Function names only useful for out
application itself, the user doesn't care about them.

####################
Jinja2, library that comes installed with Flask.
Allows us to interpolate, to put stuff (other strings) into a text - these
other strings are HTML strings.
A template is any string of text that contains placeholders for the template
language to be able to replace these placeholders with something else.
The syntax used for the placeholders, and the whole syntax of the template
as a whole, is known as a template language, and the underlying code that
evaluates the template and puts the new values in is called a template
engine.
Flask comes with the powerful Jinja2 template language.
Flask and Jinja2 were written by the same person.
