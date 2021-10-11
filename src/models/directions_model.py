from db import db
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSON

class DirectionsModel(db.Model):
    __tablename__ = 'directions_directory'

    id_direction_directory = db.Column(db.Integer, primary_key=True)
    direction_name = db.Column(db.String())
    direction_estructure = db.Column(JSON)
    geoposition = db.Column(Geometry(geometry_type='POINT', srid=4326))
    city = db.Column(db.String())
    country_code = db.Column(db.String())
    
    def __init__(self, direction_name, direction_estructure, geoposition, city, country_code):
        self.direction_name = direction_name
        self.direction_estructure = direction_estructure
        self.geoposition = geoposition
        self.city = city
        self.country_code = country_code
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    def __repr__(self):
        return f"<Direction {self.direction_name}>"

    def serialize(self):
        return {
            'direction_name': self.direction_name,
            'direction_estructure': self.direction_estructure,
            'geoposition': self.geoposition,
            'city': self.city,
            'country_code': self.country_code
        }