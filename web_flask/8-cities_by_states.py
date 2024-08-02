#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def fetch_states():
    """ Displays an HTML page with a list of all states and related cities.
    States/cities are sorted by name."""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')