#!/usr/bin/python3
""" Python script to start a flask web application
    It must listen on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """ Function to display Hello HBNB!"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=500, debug=None)
