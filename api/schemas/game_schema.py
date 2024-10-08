from api import ma
from marshmallow import Schema, fields

class GameSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'title', "descriptions", 'year')
    _id = fields.Str()
    title = fields.Str(required=True)
    descriptions = fields.Dict(required=True)
    year = fields.Int(required=True)
    
    