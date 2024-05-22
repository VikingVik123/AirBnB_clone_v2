#!/usr/bin/python3
"""
Script to start flask
"""
from flask import Flask

app = Flask(__name__)

@app.route("/",strict_slashes=False)

def hello_hbnb():
    """ returns text"""
    return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return "HBNB!"

@app.route("//c/<text>", strict_slashes=False)
def c(text):
    """ returns the value of text """
    text = text.replace("_", " ")
    return "C {}".format(text)
	

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
