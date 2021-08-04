from flask import Flask, jsonify, request
from flask_restful import Api

from resources.reddit import Reddit

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

api = Api(app)

api.add_resource(Reddit, "/reddit")


if __name__ == "__main__":
    app.run()
