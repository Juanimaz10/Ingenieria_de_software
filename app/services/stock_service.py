from app.models import Stock, ReceiptItem, Article, Receipt, ReceiptType
from app.repositories import StockRepository, BrandRepository, ArticleRepository, ReceiptRepository
from sqlalchemy import func
from app import db

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
        '''
        Calculate the total stock for a given article by summing the quantities from all receipts.
        :param article_id: ID of the article to calculate stock for.
        :return: Total stock quantity for the article.

        SQL Query:
        SELECT SUM(receipt_item.quantity * receipt_type.type_entry)
        FROM receipt_item
        JOIN receipt ON receipt_item.id_receipt = receipt.id
        JOIN receipt_type ON receipt.id_receipt_type = receipt_type.id
        WHERE receipt_item.id_article = :article_id;
        
        '''
        article = ArticleRepository.find(article_id)
        if not article:
            raise ValueError(f"Article with ID {article_id} does not exist.")
    
        total_stock = db.session.query(
            func.sum(ReceiptItem.quantity * ReceiptType.type_entry)
        ).join(
            Receipt, ReceiptItem.id_receipt == Receipt.id
        ).join(
            ReceiptType, Receipt.id_receipt_type == ReceiptType.id
        ).filter(
            ReceiptItem.id_article == article_id
        ).scalar()
    
        return total_stock if total_stock is not None else 0
    
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

   