from app.models import Stock
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository

class StockRepository(CreateAbstractRepository, ReadAbstractRepository):
    def save(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock

    def find(self, id: int) -> Stock:
        return Stock.query.get(id)

    def find_all(self) -> list[Stock]:
        return Stock.query.all()

    def find_by(self, **kwargs) -> list[Stock]:
        return Stock.query.filter_by(**kwargs).all()
