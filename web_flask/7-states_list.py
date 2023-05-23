#!/urs/bin/python3
""" A script to start a Flask web application
   It must listen at 0.0.0.0., port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def stateList():
    """ a method to display state_list html page"""
    states = storage.all()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(self):
    """ Method to delete current SQLalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
