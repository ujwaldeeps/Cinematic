from flask_restful import Resource,reqparse
from models.cast import CastModel

class Cast(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('age',
    type=int,
    required=True,
    help="field can't be empty"
    )
    parser.add_argument('movie_id',
    type=int,
    required=True,
    help="field can't be empty"
)
    def get(self,name):
        cast=CastModel.find_by_name(name)
        if cast:
            return cast.json()
        return {'message':"{} Not Found".format(name)},404

    def post(self,name):
        data=Cast.parser.parse_args()
        if CastModel.find_by_name(name):
            return {'message':"{} Not Found".format(name)},400
        cast=CastModel(name,**data)
        CastModel.save_to_db(cast)
        return cast.json()
