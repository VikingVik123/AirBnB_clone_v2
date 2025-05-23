#!/usr/bin/python3
"""
Script to start flask

/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB!"


@app.route("//c/<text>", strict_slashes=False)
def c(text):
    """ returns the value of text """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def pyt(text="is cool"):
    """ returns the value of python """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Displays a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_t(n):
    """ Displays a number """
    return render_template('5-number.html')


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_o_e(n):
    """ Checks if number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
