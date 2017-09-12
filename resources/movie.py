from flask_restful import Resource,reqparse
from models.movie import MovieModel

class MovieList(Resource):
    def get(self):
        return {'movies':[movie.json() for movie in MovieModel.query.all()]}

class Movie(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('year',
    type=int,
    required=True,
    help="field can't be empty"
    )
    parser.add_argument('rating',
    type=float,
    required=True,
    help="field can't be empty"
    )

    def get(self,name):
        movie=MovieModel.find_by_name(name)
        if movie:
            return movie.json()
        return {'message':"{} Not Found".format(name)},404

    def post(self,name):
        data=Movie.parser.parse_args()
        if MovieModel.find_by_name(name):
            return {'message':"{} Not Found".format(name)},400
        movie=MovieModel(name,**data)
        MovieModel.save_to_db(movie)
        return movie.json()
