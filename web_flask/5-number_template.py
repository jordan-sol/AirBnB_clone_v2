#!/usr/bin/python3
"""init Flask web app"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_framework():
    """ display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def disp_hbnb():
    """ display /hbnb! """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_text(text):
    """ display /c/<text> """
    return 'C %s' % text.replace('_', ' ')


@app.route("/python")
@app.route('/python/<text>/')
def py_text(text='is cool'):
    """hbnb"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def only_integer(n):
    """only integers"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def n_template(n):
    """Num of template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
