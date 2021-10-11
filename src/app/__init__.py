from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api


from db.config import config_settings
from db import db
from app.view.geocoder import PointFromDirection

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_settings['development'])
    
    api = Api(app)
    api.add_resource(PointFromDirection, '/')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    #Si queremos creat la tabla de forma automatica
    #migrate.init_app(app, db)
    
    return app