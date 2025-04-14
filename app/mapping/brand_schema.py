from marshmallow import Schema, fields, validate, post_load
from app.models import Brand

class BrandMap(Schema):
    id: int = fields.Integer(dump_only=True)
    name: str = fields.String(required=True)
    description: str = fields.String(required=True)

    @post_load
    def bind_product(self, data, **kwargs):
        return Brand(**data)