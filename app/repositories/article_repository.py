from typing import List
from app.models.article import Article
from app.repositories.base_repository import CreateAbstractRepository
from app import db

class ArticleRepository(CreateAbstractRepository):
    
    @staticmethod
    def save(article: Article) -> 'Article':
        db.session.add(article)
        db.session.commit()
        return article
    
    @staticmethod
    def delete(article: Article) -> None:
        db.session.delete(article)
        db.session.commit()

    @staticmethod
    def find(id: int) -> 'Article':
        return Article.query.get(id)
    
    @staticmethod
    def find_all() -> List[Article]:
        return Article.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List[Article]:
        return Article.query.filter_by(**kwargs).all()
    
    @staticmethod
    def update(article: Article) -> None:
        db.session.merge(article)
        db.session.commit()