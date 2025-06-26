from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str()

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str(required=True)
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    book_id = fields.Int(dump_only=True)
