from marshmallow import Schema, fields, post_load
from app.models import Category

class CategoryMap(Schema):
    id: int = fields.Integer(dump_only=True)
    name: str = fields.String(required=True)
    description: str = fields.String(required=True)

    @post_load
    def bind_product(self, data, **kwargs):
        return Category(**data)