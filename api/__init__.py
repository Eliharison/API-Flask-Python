from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

# Criando a instância do Flask
app = Flask(__name__)

# Definindo o endereço do banco
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api_games'

# Criando a instância de Api do flask_restful e passando o Flask
api = Api(app)

# Criando a instância do PyMongo
mongo = PyMongo(app)

# Criando a instância do Marshmallow
ma = Marshmallow(app)

from .resources import game_resources

