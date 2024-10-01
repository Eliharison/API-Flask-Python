from api import mongo
from ..models import game_model

# Função para cadastrar
def add_game(game):
    mongo.db.games.insert_one({
        'title' : game.title,
        'genre' : game.genre,
        'platform' : game.platform,
        'year' : game.year,
        })
    
# Função para listar os jogos
@staticmethod
def get_games():
    return list(mongo.db.games.find())