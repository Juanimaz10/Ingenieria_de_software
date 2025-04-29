from app.models import ReceiptFooter

def new_receipt_footer(total: float) -> ReceiptFooter:
    footer = ReceiptFooter()
    footer.total = total
    return footer