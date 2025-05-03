from app.models import Stock
from app.repositories import StockRepository


class StockService():
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

   