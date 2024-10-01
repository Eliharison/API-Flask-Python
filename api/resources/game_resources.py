from flask_restful import Resource
from api import api
from flask import make_response, jsonify
from ..schemas import game_schema
from ..models import game_model
from ..services import game_service


class GameList(Resource):
    def get(self):
        games = game_service.get_games()
        game = game_schema.GameSchema(many=True)
        return make_response(game.jsonify(games), 200)
    
api.add_resource(GameList, '/games')