"""
Script that starts a Flask web application & displays a value
The value can be either a string or an integer
"""


from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.errorhandler(404)
def not_found(e):
    return "Python is cool", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
