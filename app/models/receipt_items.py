from dataclasses import dataclass
from app import db


@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Modelo para representar los ítems del recibo
    """
    __tablename__ = 'receipt_items'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_article: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    quantity: int = db.Column('quantity', db.Float, nullable=False, default=0)
    id_batch: int = db.Column('id_batch', db.Integer, db.ForeignKey('batches.id'), nullable=False)
    id_receipt: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)
    receipt = db.relationship('Receipt', back_populates='items', lazy=True) 
    article = db.relationship('Article', back_populates='receipt_items', lazy=True)
    batch = db.relationship('Batch', lazy=True)