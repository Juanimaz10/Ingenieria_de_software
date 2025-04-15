from dataclasses import dataclass

from app import db



@dataclass(init=True, eq=True)
class ReceiptFooter(db.Model):
    """
    Modelo para representar el pie del recibo
    """
    __tablename__ = 'receipt_footers'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    total: float = db.Column('total', db.Float, nullable=False)

