#!/usr/bin/python3
""" Python script to start web application
    It must be listening on 0.0.0.0, port 5000
"""

from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Function to display HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to dsiplay HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function to display C followed by the value of text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ Function to display Python followed by the value of text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
