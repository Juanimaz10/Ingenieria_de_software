from app.models import ReceiptItem, Batch, Article, Receipt

def new_receipt_items(quantity: int, batch: Batch, article: Article, receipt: Receipt) -> ReceiptItem:
    item = ReceiptItem()
    item.quantity = quantity
    item.batch = batch
    item.article = article
    item.receipt = receipt
    return item