from flask import Flask
from flask_restful import Api
from .database import db
from .memoController import MemoList


def creat_app():
    app = Flask(__name__)
    app.config.from_pyfile('db.cfg')
    db.init_app(app)

    api = Api()
    api.add_resource(MemoList, '/memo')
    api.init_app(app)

    return app


if __name__ == '__main__':
    app = creat_app()
    app.run(host="0.0.0.0", port=8080)
