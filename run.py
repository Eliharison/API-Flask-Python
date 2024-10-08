# Importando o Flask que estpa em app
from api import app, mongo
from api.models.game_model import Game
from api.services.game_service import GameService

# Iniciando a aplicação co mode de depuração ativo
if __name__ == '__main__':
    # Criando o banco e a coleção se não existir
    with app.app_context():
        if 'games' not in mongo.db.list_collection_names():
            game = Game(
                title = '',
                genre = '',
                platform = '',
                year = 0
            )
            GameService.add_game(game)
            
    app.run(port=80, debug=True)