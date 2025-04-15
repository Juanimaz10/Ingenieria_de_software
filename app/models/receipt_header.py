from dataclasses import dataclass
from datetime import datetime
from app import db




@dataclass(init=True, eq=True)
class ReceiptHeader(db.Model):
    """
    Modelo para representar el encabezado del recibo
    """
    __tablename__ = 'receipt_headers'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    submission_date: datetime = db.Column('submission_date', db.DateTime, nullable=False)

  