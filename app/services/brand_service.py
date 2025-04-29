
from typing import List
from app.models import Brand
from app.repositories import BrandRepository
brand_repository = BrandRepository()

class BrandService():

    def save(brand:Brand) -> Brand:
        brand_repository.save(brand)
        return brand
    
    def delete(brand:Brand) -> None:
        brand_repository.delete(brand)

    def find(id: int) -> 'Brand':
        return brand_repository.find(id)

    def find_all() -> List['Brand']:
        return brand_repository.find_all()
    
    def find_by(**kwargs) -> List['Brand']:
        return brand_repository.find_by(**kwargs)