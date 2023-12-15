#!/usr/bin/python3
""" This script that starts a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states')
def states():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    if state is not None:
        cities = sorted(state.cities, key=lambda city: city.name)
    else:
        cities = []
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
