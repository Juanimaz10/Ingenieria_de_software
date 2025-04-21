from dataclasses import dataclass
from app import db
from app.models import Article, Receipt
from sqlalchemy.orm import Mapped




@dataclass(init=True, eq=True)
class ReceiptItem(db.Model):
    """
    Modelo para representar los ítems del recibo
    """
    __tablename__ = 'receipt_items'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_article: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    article: Mapped["Article"] = db.relationship('Article', back_populates='receipt_items', lazy=True)
    quantity: int = db.Column('quantity', db.Float, nullable=False, default=0)
    batch_id: int = db.Column('batch', db.Integer[100], nullable=False)
    receipt = db.relationship('Receipt', back_populates='items', lazy=True) 
    receipt_id: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)