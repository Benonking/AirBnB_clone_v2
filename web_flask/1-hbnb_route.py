#!/usr/bin/python3
'''
Script satrts Flask web app
listen on 0.0.0.0 port 5000
'''
from flask import Flask

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
