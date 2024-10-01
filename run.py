# Importando o Flask que estpa em app
from api import app

# Iniciando a aplicação co mode de depuração ativo
if __name__ == '__main__':
    app.run(port=80, debug=True)