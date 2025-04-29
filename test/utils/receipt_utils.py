from app.models import Receipt

def new_receipt(id_receipt_type: int, id_header: int, id_footer: int) -> Receipt:
    receipt = Receipt()
    receipt.id_header = id_header
    receipt.id_footer = id_footer
    receipt.id_receipt_type = id_receipt_type
    return receipt