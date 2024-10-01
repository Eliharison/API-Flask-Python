from api import ma
from marshmallow import Schema, fields

class GameSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'title', 'genre', 'platform', 'year')
    _id = fields.Str()
    title = fields.Str(required=True)
    genre = fields.Str(required=True)
    platform = fields.Str(required=True)
    year = fields.Str(required=True)
    
    