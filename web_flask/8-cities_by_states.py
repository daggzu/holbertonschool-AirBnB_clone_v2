#!/usr/bin/python3
""""Module set to load cities of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)  # Holds the name of the module.


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Function returns a HTML page with a list
    of states when routed to
    """
    states = storage.all(State)
    states_cities = list(states.values())
    return render_template('8-cities_by_states.html', states=states_cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
