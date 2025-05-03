from app.models import ReceiptType
from app.repositories import ReceiptTypeRepository


class ReceiptTypesService:

    @staticmethod
<<<<<<< HEAD
    def find(id: int) -> 'ReceiptType':
=======
    def find(id: int) -> ReceiptType:
>>>>>>> d52ff1e7ef99574b72bee7ccb1b4792a1f9259c6
        receipt_type = ReceiptTypeRepository.find(id)
        if not receipt_type:
                raise ValueError(f"Receipt type with ID {id} not found.")
        return receipt_type
    
    @staticmethod
    def exists(id: int) -> bool:
        return ReceiptTypeRepository.exists(id)
    