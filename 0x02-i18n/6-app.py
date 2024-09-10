#!/usr/bin/env python3
"""0x6"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ Configuring for supported languages and localization """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Return user data as query based on `login_as`"""
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Check user before ther current request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Chose the best langauge for best matching"""
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Render the '6-index.html' template"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
