#!/usr/bin/python3
""" A script that start a flask web application
   It must be listening at 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close(exc):
    """ A method to close the SQLAlchemy session."""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ A method to dispaly a HTML page."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_page("10-hbnb_filters.html", states=states,
            amenities=amenities)


if __name__ == "__main__":
    app.run(host"0.0.0.0", port=5000)
