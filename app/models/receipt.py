from dataclasses import dataclass
from app import db


@dataclass(init=True, eq=True)
class Receipt(db.Model):
    """
    Modelo para representar un recibo completo
    """
    __tablename__ = 'receipts'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_header: int = db.Column('id_receipt_header', db.Integer, db.ForeignKey('receipt_headers.id'), nullable=False)
    id_footer: int = db.Column('id_receipt_footer', db.Integer, db.ForeignKey('receipt_footers.id'), nullable=False)
    items = db.relationship('ReceiptItem', back_populates='receipt', lazy=True)
    id_receipt_type: int = db.Column('id_receipt_type', db.Integer, db.ForeignKey('receipt_types.id'), nullable=False)
    receipt_type = db.relationship('ReceiptType', lazy=True)
    

