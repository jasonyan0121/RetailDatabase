from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

db = SQLAlchemy()
DB_NAME = "retaildb"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'imgoingtoseppuku'
    app.config['SQLALCHEMY_DATABASE_URI'] =f'mysql+pymysql://root:root@localhost/{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
