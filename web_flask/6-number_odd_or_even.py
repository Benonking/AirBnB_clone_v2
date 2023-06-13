#!/usr/bin/python3
'''
Script satrts Flask web app
listen on 0.0.0.0 port 5000
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    say hello
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''
    dispay HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    retrun n id only n is a number
    '''
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_template_5(n):
    '''
    display html if n is an int
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    '''
    retrun even if n is even else odd
    '''

    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
