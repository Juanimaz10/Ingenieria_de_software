from dataclasses import dataclass
from datetime import date
from app import db


@dataclass(init=True, eq=True)
class Batch(db.Model):
    """
    Batch con sus atributos
    """
    __tablename__ = 'batches'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    code: str = db.Column('code', db.String[100], nullable=False)
    expiration_date: date = db.Column('expiration_date', db.Date, nullable=False)
    
    