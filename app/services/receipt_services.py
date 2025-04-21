from app.models import Receipt
from app.repositories import ReceiptRepository


class ReceiptService:
    """
    Service class for handling receipt-related operations.
    """

    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':
        """
        Save the receipt to the database.
        """
        # Assuming you have a database session object `db_session`
        ReceiptRepository.save(receipt)
        return receipt
    
    
    

    
    
