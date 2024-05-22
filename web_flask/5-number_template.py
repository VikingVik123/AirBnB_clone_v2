#!/usr/bin/python3
"""
Script to start flask

/number/<n>: Displays 'n is a number' only if <n> is an integer.
/number_template/<n>: Displays an HTML page only if <n> is an integer.
"""
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
