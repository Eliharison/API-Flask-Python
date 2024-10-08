from bson import ObjectId
from api import mongo
from ..models import game_model


class GameService:
    # Função para cadastrar
    def add_game(game):
        result = mongo.db.games.insert_one({
            'title': game.title,
            'genre': game.genre,
            'platform': game.platform,
            'year': game.year,
        })
        # Retorna o jogo inserido, usando o ID gerado
        return mongo.db.games.find_one({'_id': ObjectId(result.inserted_id)})

    # Função para listar os jogos
    @staticmethod
    def get_games():
        return list(mongo.db.games.find())

    @staticmethod
    def get_game_by_id(id):
        return mongo.db.games.find_one({'_id' : ObjectId(id)})

    def update_game(self, id):
        updated_game = mongo.db.games.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'title': self.title,
                'genre': self.genre,
                'platform': self.platform,
                'year': self.year,
            }},
            return_document=True
            # Garante que o documento retornado seja atualizado
        )
        return updated_game
    
    @staticmethod
    def delete_game(id):
        mongo.db.games.delete_one({'_id' : ObjectId(id)})
