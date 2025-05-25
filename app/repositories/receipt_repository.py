
from typing import List
from app.models.receipt import Receipt
from app.repositories import CreateAbstractRepository
from app import db

class ReceiptRepository(CreateAbstractRepository):
    """
    Repository class for handling database operations related to receipts.
    """

    @staticmethod
    def save(receipt: Receipt) -> 'Receipt' :
        db.session.add(receipt)
        db.session.commit()
        return receipt
    
    @staticmethod
    def find(id: int) -> 'Receipt':
        return Receipt.query.get(id)
    
    @staticmethod
    def find_by(**kwargs) -> List[Receipt]:
        return Receipt.query.filter_by(**kwargs).all()