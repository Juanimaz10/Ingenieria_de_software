from app.models import ReceiptFooter
from app.repositories import ReceiptFooterRepository


class ReceiptFooterService:
    """
    Service class for handling receipt footer-related operations.
    """

    @staticmethod
    def save(receipt_footer: ReceiptFooter) -> 'ReceiptFooter':
        return ReceiptFooterRepository.save(receipt_footer)