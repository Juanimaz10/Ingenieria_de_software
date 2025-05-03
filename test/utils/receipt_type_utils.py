from app.models import ReceiptType

def new_receipt_type(name: str, description: str, type_entry: int) -> ReceiptType:
    receipt_type = ReceiptType()
    receipt_type.name = name
    receipt_type.description = description
    receipt_type.type_entry = type_entry
    return receipt_type