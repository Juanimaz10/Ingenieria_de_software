from app.models import ReceiptType
from app.repositories import ReceiptTypeRepository


class ReceiptTypesService:

    @staticmethod
    def save(receipt_type: ReceiptType) -> 'ReceiptType':
         return ReceiptTypeRepository.save(receipt_type)

    @staticmethod
    def find(id: int) -> 'ReceiptType':
        receipt_type = ReceiptTypeRepository.find(id)
        if not receipt_type:
                raise ValueError(f"Receipt type with ID {id} not found.")
        return receipt_type
    
    @staticmethod
    def exists(id: int) -> bool:
        return ReceiptTypeRepository.exists(id)
    