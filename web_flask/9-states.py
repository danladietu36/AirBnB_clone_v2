#!/usr/bin/python3
""" A script that start a Flask web application
   It must be listening at 0.0.0.0., port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close():
    """ A method to close the SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def state():
    """ A method to display html page with state."""
    states = storage.all(State)
    return render_template("9-states.html", states=states, mode='all')


@app.route("/states/<id>", strict_slashes)
def stateId(id):
    """ A method to display html page with state and scities"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", states=states, mode=id)
        return render_template("9-states.html", states=states, mode=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0.0", port=5000)
