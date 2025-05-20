#!/usr/bin/env python3
"""Flask application setup
"""

from flask import Flask, render_template
from flask_babel import Babel
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


@app.route('/')
def index() -> Union[str, Response]:
    """Index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
