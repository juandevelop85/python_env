from db import db


class UsersModel(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    familyname = db.Column(db.String())
    id_identification_type = db.Column(db.Integer)
    id_number = db.Column(db.String())
    user = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, name, familyname, id_identification_type, id_number, user, password, email):
        self.name = name
        self.familyname = familyname
        self.id_identification_type = id_identification_type
        self.id_number = id_number
        self.user = user
        self.password = password
        self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    def __repr__(self):
        return f"<User {self.name}>"

    def serialize(self):
        return {
            'name': self.name,
            'familyname': self.familyname,
            'id_identification_type': self.id_identification_type,
            'id_number': self.id_number,
            'user': self.user,
            'password': self.password,
            'email': self.email
        }