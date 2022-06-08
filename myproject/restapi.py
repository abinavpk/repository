import flask as flask
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return {"hello": "world"}


api.add_resource(Welcome, '/hello')  # route
if __name__ == '__main__':
    app.run(debug=True)
