#!/usr/bin/python3
""" A script that start Flask web application
    It must be listening at 0.0.0.0, port=5000
"""
from flask import Flask, rendering_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ A function that display Hello HBNB!."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A function taht displays HBNB."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ A function that display C followed by value of text variable."""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_python(text="is cool"):
    """ A function that displays Python followed by value of text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_Num(n):
    """ A function to dispaly n if only n is integer."""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n=None):
    """ A function to display HTML page only if n is integer."""
    if type(n) is int:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_Num(n=None):
    """ Function to display a page only if n is integer"""
    if type(n) is int:
        if n % 2:
            num = "odd"
        else:
            num = "even"
        return render_template("6-number_odd_or_even.html", n=n, num=num)


if __name__ == "__main__":
    app.run()
