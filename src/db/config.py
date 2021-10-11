import os

class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://route-app:hCLZJWBcS1zBoaCj@localhost/planingroute'#os.getenv('SQLALCHEMY_DATABASE_URI')

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://route-app:hCLZJWBcS1zBoaCj@localhost/planingroute'#os.getenv('SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://route-app:hCLZJWBcS1zBoaCj@localhost/planingroute'#os.getenv('SQLALCHEMY_DATABASE_URI')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://route-app:hCLZJWBcS1zBoaCj@localhost/planingroute'#os.getenv('SQLALCHEMY_DATABASE_URI')

config_settings = { 'development': DevelopmentConfig }