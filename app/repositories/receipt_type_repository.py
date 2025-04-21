from app.models.receipt import Receipt
from app.models.receipt_types import ReceiptType
from app.repositories import CreateAbstractRepository
from app import db

class ReceiptTypeRepository:
    @staticmethod
    def save(receipt_type: ReceiptType) -> 'ReceiptType':
        """
        Save a new receipt type to the database.
        """
        db.session.add(receipt_type)
        db.session.commit()
        return receipt_type
    
    @staticmethod
    def get_by_id(receipt_type_id: int) -> 'ReceiptType':
        """
        Retrieve a receipt type by its ID.
        """
        return db.session.query(ReceiptType).filter_by(id=receipt_type_id).first()
    
    @staticmethod
    def get_by_receipt_id(receipt_id: int) -> 'ReceiptType':
        """
        Retrieve a receipt type by its associated receipt ID.
        """
        return db.session.query(ReceiptType).filter_by(receipt_id=receipt_id).first()
    
    @staticmethod
    def update(receipt_type: ReceiptType) -> 'ReceiptType':
        """
        Update an existing receipt type in the database.
        """
        db.session.commit()
        return receipt_type
    
    