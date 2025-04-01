
from typing import List
from app.models import Brand
from app.repositories import BrandRepository
brand_repository = BrandRepository()

class BrandService():

    def save(self, brand:Brand) -> Brand:
        brand_repository.save(brand)
        return brand
    
    def delete(self, brand:Brand) -> None:
        brand_repository.delete(brand)

    def find(self, id: int) -> 'Brand':
        return brand_repository.find(id)

    def find_all(self) -> List['Brand']:
        return brand_repository.find_all()
    
    def find_by(self, **kwargs) -> List['Brand']:
        return brand_repository.find_by(**kwargs)