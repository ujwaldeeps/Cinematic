from flask import Flask
from flask_restful import Resource,Api
from resources.cast import Cast
from resources.movie import MovieList,Movie




app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

api = Api(app)

app.secret_key = 'ujwal'

@app.before_first_request
def tables():
    db.create_all()




api.add_resource(Cast,'/cast/<string:name>')
api.add_resource(MovieList,'/movies')
api.add_resource(Movie,'/movie/<string:name>')


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
