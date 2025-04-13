from marshmallow import Schema, fields, post_load
from app.models import Article


class ArticleMap(Schema):

    id_article: int =  fields.Integer(dump_only=True)
    name: str = fields.String(required=True)
    description: str =  fields.String(required=True)
    category: str =  fields.String(required=True)
    brand: str =  fields.String(required=True)
    minimun_stock: float =  fields.Float(required=True)
    code_ean13: str =  fields.String(required=True)


    @post_load
    def bind_article(self, data, **kwargs):
        return Article(**data)