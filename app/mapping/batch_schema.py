from marshmallow import Schema, fields, post_load
from datetime import date
from app.models import Batch


class BatchMap(Schema):

    id_batch: int =  fields.Integer(dump_only=True)
    code: str =  fields.String(required=True)
    expiration_date: date = fields.Date(required=True)


    @post_load
    def bind_batch(self, data, **kwargs):
        return Batch(**data)