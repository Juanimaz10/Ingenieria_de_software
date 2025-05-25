from app.models import ReceiptHeader
from app.repositories import ReceiptHeaderRepository


class ReceiptHeaderService:

    @staticmethod
    def save(receipt_header: ReceiptHeader) -> 'ReceiptHeader':
        return ReceiptHeaderRepository.save(receipt_header)