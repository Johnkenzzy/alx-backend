#!/usr/bin/env python3
"""Flask application setup
"""

from flask import Flask, render_template
from typing import Union
from werkzeug.wrappers import Response


app = Flask(__name__)


@app.route('/')
def index() -> Union[str, Response]:
    """Index route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
