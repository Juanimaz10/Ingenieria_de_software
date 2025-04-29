from app.models import ReceiptType
from app.repositories import ReceiptTypeRepository


class ReceiptTypesService:

    @staticmethod
    def find(id: int) -> 'ReceiptTypeRepository':
        receipt_type = ReceiptType.find(id)
        if not receipt_type:
                raise ValueError(f"Receipt type with ID {id} not found.")
        return receipt_type
    