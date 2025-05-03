from app.models import Receipt, ReceiptType

def new_receipt(receipt_type: ReceiptType, id_header: int, id_footer: int) -> Receipt:
    receipt = Receipt()
    receipt.id_header = id_header
    receipt.id_footer = id_footer
    receipt.receipt_type = receipt_type
    

    return receipt