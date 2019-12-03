from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class ReverseString(Resource):
    def post(self):
        parser.add_argument('string', type=str)
        args = parser.parse_args()
        return args['string'][::-1]

class CheckString(Resource):
    def post(self):
        parser.add_argument('string', type=str)
        args = parser.parse_args()
        return {
            'hasUpper': hasUpper(args['string']),
            'hasLower': hasLower(args['string']),
            'hasNumbers': hasNumbers(args['string']),
            'hasSpecial': hasSpecial(args['string'])
            }

def hasUpper(inputString):
    return any(char.isupper() for char in inputString)

def hasLower(inputString):
    return any(char.islower() for char in inputString)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasSpecial(inputString):
    return any(not char.isalnum() for char in inputString)

api.add_resource(ReverseString, '/reverse')
api.add_resource(CheckString, '/check')

if __name__ == '__main__':
     app.run(port='5002')
