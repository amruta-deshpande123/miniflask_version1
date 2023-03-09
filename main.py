"""
# STEPS


1. Create a new project in Pycharm and name the project as `miniflask_version1`
2. Make sure `venv` is created
3. Install Flask (copy instruction from Pypi)
4. `pip freeze > requirements.txt`
5. Create `README.md` file and write down project structure
6. Write first Flask application in `main.py` file.

Hello world application of Flask
"""

from flask import Flask

# `Flask` is a class we use to instantiate an application
app = Flask(__name__)


# First http GET request
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

# SECOND http GET request
@app.route("/greeting")
def custom_message():

    import requests

    response = requests.get("https://swapi.dev/api/films/1")
    # store response in DB
    return "<h1>data has been saved in DB</h1"
