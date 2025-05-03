from app.models import ReceiptFooter
from app.repositories import ReceiptFooterRepository


class ReceiptFooterService:
    """
    Service class for handling receipt footer-related operations.
    """

    @staticmethod
    def get_all_receipt_footers(ReceiptFooter: ReceiptFooter) -> list[ReceiptFooter]:
        """
        Retrieve all receipt footers.
        """
        return ReceiptFooterRepository.get_all_receipt_footers(ReceiptFooter)
    
    @staticmethod
    def get_receipt_footer_by_id(receipt_footer_id: int) -> 'ReceiptFooter':
        """
        Retrieve a receipt footer by its ID.
        """
        return ReceiptFooterRepository.get_receipt_footer_by_id(receipt_footer_id)
    
    @staticmethod
    def create_receipt_footer(receipt_footer_data: dict) -> 'ReceiptFooter':
        """
        Create a new receipt footer.
        """
        return ReceiptFooterRepository.create_receipt_footer(receipt_footer_data)
    
    @staticmethod
    def update_receipt_footer(receipt_footer_id: int, updated_data: dict) -> 'ReceiptFooter':
        """
        Update an existing receipt footer.
        """
        return ReceiptFooterRepository.update_receipt_footer(receipt_footer_id, updated_data)
    
    @staticmethod
    def delete_receipt_footer(receipt_footer_id: int) -> None:
        """
        Delete a receipt footer.
        """
        return ReceiptFooterRepository.delete_receipt_footer(receipt_footer_id)