#!/usr/bin/python3
""" A python script that starts a Flask web application
    It must be listening at 0.0.0.0 port 5000
"""


from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Function to display Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function to display HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def text():
    """Function to display C followed by text variable's value"""
    return ("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
