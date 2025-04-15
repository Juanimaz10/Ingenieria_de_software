from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=True)
class ReceiptType(db.Model):
    """
    Modelo para representar el tipo de recibo
    """
    __tablename__ = 'receipt_types'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String(100), nullable=False)
    description: str = db.Column('description', db.String(150), nullable=True)
    type_entry: int = db.Column('type_entry', db.Integer, nullable=False)
