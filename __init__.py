# external libraries
from flask import Flask
from database import init_db

# internal libraries
from routes import pages


app = Flask(__name__)


def getApp():
    return app


if __name__ == '__main__':
    SERVER_ROOT = '127.0.0.1' # local host
    app.debug = True

    # register all relevant routes to the application
    app.register_blueprint(pages)

    # startup database connection
    init_db()

    app.run(host=SERVER_ROOT)