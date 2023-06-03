
Simple html/css, python, flask and jinja2 examples run on local machine

####################
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
    pyenv exec python -m venv .venv (add .venv to gitignore)
    # activate the virtual environment

(3) Activate pyenv
    .\.venv\Scripts\activate

(4) Install Flask (into the virtual environment)
    pip install Flask

(5) Write Flask app in file app.py (default for Flask)

    from flask import Flask
    app = Flask(__name__)
    @app.route("/")
    def hello_world():
        return "Hello, world!"

(6) Set flask environment variables (powershell)
    # Tell Flask before we run it which python file contains the Flask app
    $env:FLASK_APP = "app.py"
    $env:FLASK_APP
    $env:FLASK_DEBUG = 1
    $env:FLASK_DEBUG
Environment variables are deleted by setting them to null:
$env:TEST_VAR = 1 (create and set to 1)
$env:TEST_VAR = $null (delete)

(7) Now we can run flask
    flask run

(8) MongoDB / Cloud Atlas / pymongo
    See Mongo Cloud Atlas notes below
    VPN: need to add vpn address to Network Access in Cloud Atlas or
    will get pymongo connection timeout errors

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

####################
Final Forward Slashe in @app.route endpoints.
Endpoint of: @app.route("/home/") is better to use than:
@app.route("/home") because typing URL of
https://www.example.com/home or https://www.example.com/home/
will take you to the expected page. 

Endpoint of: @app.route("/home") would result in only
https://www.example.com/home working with 
https://www.example.com/home/ failing.

####################
Jinja2
Interpolate: "to insert between other elements or parts" 
{{ }}   expressions, these will get reduced to a single value and
        get interpolated into the template
{% %}   statements, allow Jinja2 tp make decisions or do something
        other than interpolating values (if, for)

####################
Teclado website 18k hits per month, most ever simultaneous POSTS is 5


####################
MongoDB Cloud Atlas
MongoDB originally designed for large amounts of small pieces data
**MongoDB Cloud Atlas (DB in the cloud, DBaaS, DB as a Service)
**MongoDB Compass (local GUI for managing our DBs in the cloud)
MongoDB Collections of Documents (CD)

No schema needed in mDB so easy to store a lot of info without
lots of design considerations (unlike schema based SQL) but
this also means you cannot do joins to see relationships between
tables / do multiple checks like SQL cam
SQL creates relations between tables via PKs and FKs

{JSON} = 1 document
[{JSON1}, {JSON2}] = multiple documents (list of documents)

A mDB document is "like" a row in a SQL table. A collection
of documents is "like" a SQL table

** pip install pymongo[srv] # in pyenv 3.9.0  
# srv part need to connect to cloud atlas

pip freeze # see everything you've installed with pip
mongodb+srv://mong-rabbit:<password>@jack-rabbit.u44ibnh.mongodb.net/
Replace all of <password> with the password (remove < > too)

"jack-rabbit" is a mongoDB atlas CLUSTER
via USER "mong-rabbit" & passwd ****.
An atlas cluster can be though of as a cloud server
User "mong-rabbit" was created on the cloud atlas website,


####################
Portfolio
Drum: Flexbox and media query added for responsiveness. Sass used.
Dice: Storing results in local storage "database". Media query responsiveness. Sass used.
Simon: Flexbox and media query for responsiveness (fixed inline-block blue line issue). Sass added. 

####################
Environment (in pyenv)
pip install python-dotenv
