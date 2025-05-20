#!/usr/bin/env python3
"""Flask application setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union, List
from werkzeug.wrappers import Response


app = Flask(__name__)


class Config:
    """App configuration class"""
    LANGUAGES: List = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get the set local langauge"""
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


@app.route('/')
def index() -> Union[str, Response]:
    """Index route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
