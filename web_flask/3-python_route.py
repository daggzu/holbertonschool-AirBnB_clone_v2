#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask
app = Flask(__name__)  # Holds the name of the module.


@app.route('/', strict_slashes=False)  # Maps the root route.
def hello_hbnb():
    """Function returns a string when routed to"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)  # Maps the /hbnb route.
def hbnb():
    """Function returns a string when routed to"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)  # Maps the /c/<text> route.
def c(text):
    """Function returns a string when routed to"""
    return "C {}".format(text.replace("_", " "))


# Maps the /python route.
@app.route('/python', strict_slashes=False)
# Maps the /python/<text> route.
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Function returns a string when routed to"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
