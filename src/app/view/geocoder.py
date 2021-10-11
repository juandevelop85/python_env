from flask import make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource
from models.UserModel import UsersModel
from app.view.clean_direction import FindLatLonByDirtext

parser = reqparse.RequestParser()
parser.add_argument('id_file', type=int)

class PointFromDirection(Resource):
    # def get(self):
    #     response = {
    #         'message': 'Hola',
    #         'response': [],
    #         'geo': []
    #     }
    #     #print(user)
    #     try:
    #         user = UsersModel.query.all()
    #         userJson = [e.serialize() for e in user]
    #         response['response'] = userJson
    #         print(userJson)
    #         return make_response(jsonify(response), 200)
    #     except Exception as e:
    #         return(str(e))       

    def post(self):
        args = parser.parse_args()
        id_file = int(args['id_file'])
        response = {
            'message': 'Hola',
            'response': [],
            'geo': []
        }
        #print(user)
        try:
            geo = FindLatLonByDirtext(id_file)
            response['geo'] = geo
            print(id_file)
            return make_response(jsonify(response), 200)
        except Exception as e:
            return(str(e))     
