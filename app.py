import pymysql
from flask import Flask
from model.user_dao import UserDao
from service.user_service import UserService
from view import create_endpoints


class Services:
    pass


def create_app(test_config=None):
    app = Flask(__name__)
    app.debug = True

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = pymysql.connect()

    user_dao = UserDao(database)

    services = Services
    services.user_service = UserService(user_dao, app.config)

    user_service = UserService(user_dao, app.config)

    create_endpoints(app, services)

    return app