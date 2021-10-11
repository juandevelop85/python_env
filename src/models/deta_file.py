from db import db
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSON

class DetaFile(db.Model):
    __tablename__ = 'deta_file'

    id_detafile = db.Column(db.Integer, primary_key=True)
    id_file = db.Column(db.Integer)
    address = db.Column(db.String())
    suburb = db.Column(db.String())
    post_code = db.Column(db.String())
    region = db.Column(db.String())
    mobile_phone = db.Column(db.String())
    email = db.Column(db.String())
    driver = db.Column(db.String())
    comments = db.Column(db.String())
    
    def __init__(self, id_file, address, suburb, post_code, region, mobile_phone, email, driver, comments):
        self.id_file = id_file
        self.address = address
        self.suburb = suburb
        self.post_code = post_code
        self.region = region
        self.mobile_phone = mobile_phone
        self.email = email
        self.driver = driver
        self.comments = comments
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    def __repr__(self):
        return f"<Direction {self.address}>"

    def serialize(self):
        return {
            'id_file': self.id_file,
            'address': self.address,
            'suburb': self.suburb,
            'post_code': self.post_code,
            'region': self.region,
            'mobile_phone': self.mobile_phone,
            'email': self.email,
            'driver': self.driver,
            'comments': self.comments
        }