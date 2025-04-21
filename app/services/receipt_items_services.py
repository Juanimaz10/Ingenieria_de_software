from app.models import ReceiptItems
from app.repositories import ReceiptItemsRepository
from app.models import ReceiptType


class ReceiptItemsService:
    """
    Service class for handling receipt item-related operations.
    """

    @staticmethod
    def get_all_receipt_items(ReceiptType: ReceiptType) -> list[ReceiptType]:
        """
        Retrieve all receipt items.
        """
        return ReceiptItemsRepository.get_all_receipt_items(ReceiptType)

    @staticmethod
    def get_receipt_item_by_id(receipt_item_id: int) -> 'ReceiptType':
        """
        Retrieve a receipt item by its ID.
        """
        return ReceiptItemsRepository.get_receipt_item_by_id(receipt_item_id)

    @staticmethod
    def create_receipt_item(receipt_item_data: dict) -> 'ReceiptType':
        """
        Create a new receipt item.
        """
        return ReceiptItemsRepository.create_receipt_item(receipt_item_data)

    @staticmethod
    def update_receipt_item(receipt_item_id: int, updated_data: dict) -> 'ReceiptType':
        """
        Update an existing receipt item.
        """
        return ReceiptItemsRepository.update_receipt_item(receipt_item_id, updated_data)

    @staticmethod
    def delete_receipt_item(receipt_item_id: int) -> None:
        """
        Delete a receipt item.
        """
        return ReceiptItemsRepository.delete_receipt_item(receipt_item_id)