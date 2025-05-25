from app.models import Stock, ReceiptItem, Article
from app.repositories import StockRepository, BrandRepository, ArticleRepository, ReceiptRepository


class StockService():

    @staticmethod
    def register(stock: Stock) -> Stock:
        article = ArticleRepository.find(stock.article.id)
        if not article:
            raise ValueError(f"Article with ID {stock.article.id} does not exist.")

        receipt = ReceiptRepository.find(stock.receipt.id)
        if not receipt:
            raise ValueError(f"Receipt with ID {stock.receipt.id} does not exist.")

        brand = BrandRepository.find(article.brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {article.brand_id} does not exist.")
        return StockRepository.save(stock)

    @staticmethod
    def calculate_stock(article_id: int) -> int:
        article = ArticleRepository.find(article_id)
        if not article:
            raise ValueError(f"Article with ID {article_id} does not exist.")
        
        receipt_items = ReceiptItem.query.filter_by(id_article=article_id).all()

        total_stock = 0
        for item in receipt_items:
            type_entry = item.receipt.receipt_type.type_entry
            total_stock += item.quantity * type_entry

        return total_stock
    
    @staticmethod
    def save(stock: Stock) -> Stock:
        return StockRepository.save(stock)
    
    @staticmethod
    def register(stock: Stock) -> Stock:
        return StockRepository.save(stock)

    @staticmethod
    def find(id_stock: int) -> Stock:
        return StockRepository.find(id_stock)

    @staticmethod
    def find_all() -> list[Stock]:
        return StockRepository.find_all()

    @staticmethod
    def find_by(**kwargs) -> list[Stock]:
        return StockRepository.find_by(**kwargs)

   