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
    """ list of all State objects present in DBStorage sorted by name"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')