
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

    