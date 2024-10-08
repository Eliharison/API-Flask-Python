from api import mongo

class Game():
    def __init__(self, title, descriptions, year):
        self.title = title
        self.descriptions = descriptions
        self.year = year
        