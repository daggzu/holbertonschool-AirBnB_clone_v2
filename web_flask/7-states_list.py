#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)  # Holds the name of the module.


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Function returns a HTML page with a list
    of states when routed to
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
