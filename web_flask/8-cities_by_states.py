#!/usr/bin/python3
""" A script to start flask web application
   It must be listening at 0.0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ A method to close SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    """ A method to display html containing list of cities"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
