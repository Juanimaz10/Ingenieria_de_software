from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=True)
class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_article: int = db.Column('id_article', db.Integer, db.ForeignKey('articles.id'), nullable=False)
    id_receipt: int = db.Column('id_receipt', db.Integer, db.ForeignKey('receipts.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    id_batch: int = db.Column('id_batch', db.Integer, db.ForeignKey('batches.id'), nullable=False)
    article = db.relationship('Article', lazy=True)
    batch = db.relationship('Batch', lazy=True)
    receipt = db.relationship('Receipt', lazy=True) 
   