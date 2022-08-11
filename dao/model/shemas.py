from marshmallow import Schema, fields

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Integer()
    rating = fields.Float()
    genre = fields.Nested('GenreSchema')
    director = fields.Nested('DirectorSchema')

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()