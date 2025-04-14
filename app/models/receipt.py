from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass(init=True, eq=True)
class ReceiptType(db.Model):
    """
    Modelo para representar el tipo de recibo
    """
    __tablename__ = 'receipt_types'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String[100], nullable=False)
    description: str = db.Column('description', db.String[150], nullable=True)
    type: int = db.Column('type', db.Integer, nullable=False)

@dataclass(init=True, eq=True)
class ReceiptHeader(db.Model):
    """
    Modelo para representar el encabezado del recibo
    """
    __tablename__ = 'receipt_headers'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    submission_date: datetime = db.Column('submission_date', db.DateTime, nullable=False)

@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Modelo para representar los ítems del recibo
    """
    __tablename__ = 'receipt_items'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_article: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    quantity: float = db.Column('quantity', db.Float, nullable=False)
    batch: str = db.Column('batch', db.String[100], nullable=True)

@dataclass(init=True, eq=True)
class ReceiptFooter(db.Model):
    """
    Modelo para representar el pie del recibo
    """
    __tablename__ = 'receipt_footers'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    total: float = db.Column('total', db.Float, nullable=False)

@dataclass(init=True, eq=True)
class Receipt(db.Model):
    """
    Modelo para representar un recibo completo
    """
    __tablename__ = 'receipts'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_receipt_header: int = db.Column('id_receipt_header', db.Integer, db.ForeignKey('receipt_headers.id'), nullable=False)
    id_receipt_footer: int = db.Column('id_receipt_footer', db.Integer, db.ForeignKey('receipt_footers.id'), nullable=False)
    id_receipt_items: list[ReceiptItem] = db.relationship('ReceiptItem', backref='receipt', lazy=True)
    id_receipt_type: int = db.Column('id_receipt_type', db.Integer, db.ForeignKey('receipt_types.id'), nullable=False)