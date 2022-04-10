from marshmallow import fields
from app.exet import ma

class CarSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    model = fields.String()
    price = fields.Float()
    year = fields.String()
    color = fields.String()
    brand = fields.Nested('BrandSchema', many=True)

class BrandSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()