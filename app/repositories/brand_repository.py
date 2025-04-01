from typing import List
from app.models import Brand
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class BrandRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):

    def save(self, brand:Brand) -> Brand:
        db.session.add(brand)
        db.session.commit()
        return brand
    
    def delete(self, brand:Brand) -> None:
        db.session.delete(brand)
        db.session.commit()
    
    def find(self, id: int) -> 'Brand':
        return Brand.query.get(id)

    def find_all(self, ) -> List['Brand']:
        return Brand.query.all()
    
    def find_by(self, **kwargs) -> List['Brand']:
        return Brand.query.filter_by(**kwargs).all()
    