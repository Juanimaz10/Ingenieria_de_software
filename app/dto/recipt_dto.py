from dataclasses import dataclass
from app.dto import ReceiptItemDTO
from app.models import ReceiptFooter, ReceiptHeader


@dataclass
class ReceiptDTO:
    header: ReceiptHeader
    items: list['ReceiptItemDTO'] 
    Footer: ReceiptFooter
    id_receipt_type: int
