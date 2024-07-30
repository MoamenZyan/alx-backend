#!/usr/bin/env python3
"""
Flask app
"""
from typing import (Union, Dict)

from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import g, request


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


# Users info
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Check user details
    Args:
        id (str): user's id
    Returns: 
        dictionary if valid
    """
    return users.get(int(id), {})


@babel.localeselector
def get_locale() -> str:
    """
    My script
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.before_request
def before_request() -> None:
    """
    Add valid user
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render HTML Page
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
