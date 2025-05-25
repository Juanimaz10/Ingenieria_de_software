from app.models import Stock, Article, Batch, Receipt

def new_stock(article: Article, batch: Batch, receipt: Receipt, quantity:int) -> Stock:
    stock = Stock()
    stock.article = article
    stock.batch = batch
    stock.receipt = receipt
    stock.quantity = quantity
    return stock

