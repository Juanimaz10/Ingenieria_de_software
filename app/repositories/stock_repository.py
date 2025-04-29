from app.models import Stock
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository

class StockRepository(CreateAbstractRepository, ReadAbstractRepository):
    @staticmethod
    def save(stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    @staticmethod
    def find( id: int) -> Stock:
        return Stock.query.get(id)
    
    @staticmethod
    def find_all() -> list[Stock]:
        return Stock.query.all()
    
    @staticmethod
    def find_by( **kwargs) -> list[Stock]:
        return Stock.query.filter_by(**kwargs).all()
