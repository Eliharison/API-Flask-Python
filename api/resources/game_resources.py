from flask_restful import Resource
from api import api


class GameList(Resource):
    def get(self):
        return {"Hello World": "Api Rodando"}
    
class RecursosAPI(Resource):
    def get(self):
        return {"Olá": "Você enviou um Request GET"}
    
    def post(self):
        return "Você fez um método POST"
    
    def put(self):
        return "Você fez um método PUT"
    
    def  delete(self):
        return "Você deletou algo, não sei o que"
    
api.add_resource(GameList, '/games')
api.add_resource(RecursosAPI, '/resources')