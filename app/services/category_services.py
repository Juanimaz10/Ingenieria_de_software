from app.models import Category
from app.repositories import CategoryRepository
from typing import List


class CategoryService():
    
    def save(category: Category) -> 'Category':
        CategoryRepository.save(category)
        return category
    
    def delete(category: 'Category') -> None:
        CategoryRepository.delete(category)

    def find(id: int) -> 'Category':
        return CategoryRepository.find(id)
    
    def find_all() -> List['Category']:
        return CategoryRepository.find_all()
    
    def find_by(**kwargs) -> List['Category']:
        return CategoryRepository.find_by(**kwargs)
    
    def update(category: 'Category') -> 'Category':
        CategoryRepository.update(category)
        return category