from app.models import Stock
from app.repositories import StockRepository
stock_repository = StockRepository()

class StockService():
    @staticmethod
    def save(stock: Stock) -> Stock:
        return stock_repository.save(stock)
    
    @staticmethod
    def register(stock: Stock) -> Stock:
        return stock_repository.save(stock)

    @staticmethod
    def find(id_stock: int) -> Stock:
        return stock_repository.find(id_stock)

    @staticmethod
    def find_all() -> list[Stock]:
        return stock_repository.find_all()

    @staticmethod
    def find_by(**kwargs) -> list[Stock]:
        return stock_repository.find_by(**kwargs)

   