from app.models import ReceiptHeader
from app.repositories import ReceiptHeaderRepository


class ReceiptHeaderServices:
    @staticmethod
    def get_all_receipt_headers(ReceiptHeader: ReceiptHeader) -> list[ReceiptHeader]:
        """Retrieve all receipt headers."""
        return ReceiptHeaderRepository.get_all_receipt_headers(ReceiptHeader)
    
    @staticmethod
    def get_receipt_header_by_id(receipt_header_id: int) -> 'ReceiptHeader':
        """Retrieve a receipt header by its ID."""
        return ReceiptHeaderRepository.get_receipt_header_by_id(receipt_header_id)
    
    @staticmethod
    def create_receipt_header(receipt_header_data: dict) -> 'ReceiptHeader':
        """Create a new receipt header."""
        return ReceiptHeaderRepository.create_receipt_header(receipt_header_data)
    
    @staticmethod
    def update_receipt_header(receipt_header_id: int, updated_data: dict) -> 'ReceiptHeader':
        """Update an existing receipt header."""
        return ReceiptHeaderRepository.update_receipt_header(receipt_header_id, updated_data)
    
    @staticmethod
    def delete_receipt_header(receipt_header_id: int) -> None:
        """Delete a receipt header."""
        return ReceiptHeaderRepository.delete_receipt_header(receipt_header_id)
    