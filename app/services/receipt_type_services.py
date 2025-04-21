from app.models import ReceiptType
from app.repositories import ReceiptTypeRepository


class ReceiptTypesService:

    """
    Service class for handling receipt type-related operations.
    """

    @staticmethod
    def get_all_receipt_types(ReceiptType: ReceiptType) -> list[ReceiptType]:
        """
        Retrieve all receipt types.
        """
        return ReceiptTypeRepository.get_all_receipt_types(ReceiptType)
    
    @staticmethod
    def get_receipt_type_by_id(receipt_type_id: int) -> 'ReceiptType':
        """
        Retrieve a receipt type by its ID.
        """
        return ReceiptTypeRepository.get_receipt_type_by_id(receipt_type_id)
    
    @staticmethod
    def create_receipt_type(receipt_type_data: dict) -> 'ReceiptType':
        """
        Create a new receipt type.
        """
        return ReceiptTypeRepository.create_receipt_type(receipt_type_data)
    
    @staticmethod
    def update_receipt_type(receipt_type_id: int, updated_data: dict) -> 'ReceiptType':
        """
        Update an existing receipt type.
        """
        return ReceiptTypeRepository.update_receipt_type(receipt_type_id, updated_data)
    
    @staticmethod

    def delete_receipt_type(receipt_type_id: int) -> None:
        """
        Delete a receipt type.
        """
        return ReceiptTypeRepository.delete_receipt_type(receipt_type_id)