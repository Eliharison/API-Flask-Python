from api import mongo

class Game():
    def __init__(self, title, genre, platform, year):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.year = year
        