from typing import List
from app.models import Category
from app import db


class CategoryRepository():
    
    def save(category: Category) -> 'Category':
        db.session.add(category)
        db.session.commit()
        return category
    
    def delete(category: Category) -> None:
        db.session.delete(category)
        db.session.commit()

    def find(id: int) -> 'Category':
        return Category.query.get(id)
    
    def find_all() -> List[Category]:
        return Category.query.all()
    
    def find_by(**kwargs) -> List[Category]:
        return Category.query.filter_by(**kwargs).all()
    
    def update(category: Category) -> None:
        db.session.merge(category)
        db.session.commit()