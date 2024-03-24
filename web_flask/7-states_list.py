#!/usr/bin/python3
"""task 7 of web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Display 'HBNB'
        """
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """c def
        """
        return 'C ' + text.replace('_', ' ')

    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        """python def
        """
        return 'Python ' + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """number def
        """
        return str(n) + ' is a number'

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """number_temp def
        """
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """number_odd def
        """
        parity = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """states_list def
        """
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)

    @app.teardown_appcontext
    def teardown_db(error):
        """Closes the database 
        """
        storage.close()

    app.run('0.0.0.0')
