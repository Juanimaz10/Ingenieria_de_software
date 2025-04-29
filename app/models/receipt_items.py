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
    batch_id: int = db.Column('id_batch', db.Integer, db.ForeignKey('batches.id'), nullable=False)
    receipt_id: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)

    batch = db.relationship('Batch', back_populates='batch', lazy=True)
    receipt = db.relationship('Receipt', back_populates='items', lazy=True) 
    article = db.relationship('Article', back_populates='receipt_items', lazy=True)