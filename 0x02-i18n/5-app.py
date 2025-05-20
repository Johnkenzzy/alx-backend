#!/usr/bin/env python3
"""Flask application setup
"""

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, List, Dict
from werkzeug.wrappers import Response

app: Flask = Flask(__name__)


class Config:
    """App configuration class"""
    LANGUAGES: List = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel: Babel = Babel(app)

# Mock user "database"
users: Dict = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> int:
    """Get user from URL param"""
    try:
        user_id: int = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set user in Flask global before each request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Get the set local langauge"""
    locale: str = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.get("user"):
        user_locale = g.user.get("locale")
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> Union[str, Response]:
    """Index route"""
    return render_template('5-index.html', current_locale=str(get_locale()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
