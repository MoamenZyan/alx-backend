#!/usr/bin/env python3

"""
Flask app
"""

from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render HTML Page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
