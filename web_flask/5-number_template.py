#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask, render_template
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


# Maps the /number/<n> route.
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function returns a string with an integer when routed to"""
    return "{:d} is a number".format(n)


# Maps the /number_template/<n> route.
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Function returns a HTML page when an integer is given."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
