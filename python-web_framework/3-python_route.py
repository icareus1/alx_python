"""Script that starts a Flask web application & displays a value(str)"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    ftext = text.replace('_', ' ')
    return f'C {ftext}'


@app.route('/python/<text>', strict_slashes=False)
def the_p_snake(text=None):
    if text is None:
        text = 'is cool'
    try:
        ftext = text.replace('_', ' ')
        return f'Python {ftext}'
    except Exception as e:
        return 'Python is cool'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
