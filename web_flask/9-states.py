#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Function returns a HTML page with a
    list of states when routed to.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """
    Function returns a HTML page with a
    list of states when routed to.
    """
    state = storage.get(State, id)
    if state is not None:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-state.html',
                               state=state, cities=cities)
    else:
        return render_template('404.html'), 404


@app.teardown_appcontext
def teardown_db(self):
    """Method for closing Flask connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
