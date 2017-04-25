from flask import Flask
from flask_restful import Api
from flask.ext.pymongo import PyMongo
from flask_cors import CORS

app = Flask("clicksocial")
api = Api(app)
mongo = PyMongo(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

import clicksocial.views