from flask import Flask


def create_app():
    """
    This is a comment on python.This app is using the app factory pattern.
    """
    """
    Create an instance of the flask app.
    """
    app = Flask(__name__, instance_relative_config=True)

    """
    Load custom application settings.
    """

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    """
    Creates a route(endpoint) that maps to the Home page app.The index function will be excecuted when someone visit this route.
    It just renders a hello world response.flask will render the response as html content as long with a status code of 200 which means 
    sucess.
    """

    @app.route('/')
    def index():

        return app.config['HELLO']
    """
    Return the instance of the flask application.
    """
    return app
