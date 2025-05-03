from typing import List
from app.models.receipt import Receipt
from app.models.receipt_types import ReceiptType
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

from app import db

class ReceiptTypeRepository(CreateAbstractRepository,ReadAbstractRepository,DeleteAbstractRepository):
   
    @staticmethod
    def save(receipt_type:ReceiptType) -> 'ReceiptType':
        db.session.add(receipt_type)
        db.session.commit()
        return ReceiptType
    
    @staticmethod
    def delete(receipt_type:ReceiptType) -> None:
        db.session.delete(receipt_type)
        db.session.commit()

    @staticmethod
    def find(id: int) -> 'ReceiptType':
        return ReceiptType.query.get(id)
    
    @staticmethod
    def find_all() -> List['ReceiptType']:
        return ReceiptType.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List['ReceiptType']:
        return ReceiptType.query.filter_by(**kwargs).all()
    
    @staticmethod
    def exists(id: int) -> bool:
        return ReceiptType.query.get(id) is not None
    