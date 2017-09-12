from db import db
class MovieModel(db.Model):
    __tablename__="movies"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    year=db.Column(db.Integer)
    rating=db.Column(db.Float(precision = 2))


    cast=db.relationship('CastModel',lazy='dynamic')

    def __init__(self,name,year,rating):
        self.name=name
        self.year=year
        self.rating=rating

    def json(self):
        return {'name':self.name,'year':self.year,'rating':self.rating,'cast':[cast.json() for cast in self.cast.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
