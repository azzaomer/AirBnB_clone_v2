#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'

@app.route("/", strict_slashes=False)
def hello_world():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')i
