#!/usr/bin/python3
"""Module starts a Flask web application"""
from flask import Flask
app = Flask(__name__)  # Holds the name of the module.


@app.route('/', strict_slashes=False)  # Maps the root route.
def hello_hbnb():
    """Function returns a string when routed to"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs the application.
