#!/usr/bin/env python3
""" Using babel flask for i13n """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Set Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Returning accept_languages paramter for best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ Rendering the template (1-index.html) """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
