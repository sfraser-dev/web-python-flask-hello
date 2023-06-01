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
