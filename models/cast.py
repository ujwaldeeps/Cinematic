from db import db


class CastModel(db.Model):
    __tablename__="cast"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.id'))

    movie=db.relationship('MovieModel')
    def __init__(self,name,age,movie_id):
        self.name=name
        self.age=age
        self.movie_id=movie_id

    def json(self):
        return {'name':self.name,'age':self.age}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
