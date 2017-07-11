from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_admin import Admin
from flask_babelex import Babel


app = Flask("clicksocial")
app.config['SECRET_KEY'] = "clicksocial"
api = Api(app)
mongo = PyMongo(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
admin = Admin(app, 'clicksocial', template_mode='bootstrap3')
babel = Babel(app)

import views
