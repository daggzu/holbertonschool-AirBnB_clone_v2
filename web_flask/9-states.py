#!/usr/bin/python3
"""Module starts a Flask web application"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """
    Function returns an HTML page with a list of states when routed to.
    
    Retrieves the list of states from the data storage, sorts them by name,
    and passes the sorted list to the '9-states.html' template for rendering.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """
    Function returns an HTML page with information about a specific state when routed to.
    
    Retrieves the state with the given ID from the data storage. If the state
    exists, retrieves and sorts its cities by name, and passes the state and
    cities to the '9-state.html' template for rendering. If the state does not
    exist, it returns a 404 error using the '404.html' template.
    """
    state = storage.get(State, id)
    if state is not None:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return render_template('404.html'), 404

@app.teardown_appcontext
def teardown_db(self):
    """
    Method for closing the Flask connection.
    
    This function is automatically called when the Flask app context is torn
    down. It ensures that the data storage (assumed to be a database) is closed
    when the application is shut down or the request context is popped.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
