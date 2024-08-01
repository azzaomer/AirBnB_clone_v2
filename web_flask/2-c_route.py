#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def text_c(text):
    """display “C ” followed by the value of the text"""
    return f'C_{text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')