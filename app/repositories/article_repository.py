from typing import List
from app.models import Article
from app import db


class ArticleRepository():
    
    def save(article: Article) -> 'Article':
        db.session.add(article)
        db.session.commit()
        return article
    
    def delete(article: Article) -> None:
        db.session.delete(article)
        db.session.commit()

    def find(id: int) -> 'Article':
        return Article.query.get(id)
    
    def find_all() -> List[Article]:
        return Article.query.all()
    
    def find_by(**kwargs) -> List[Article]:
        return Article.query.filter_by(**kwargs).all()
    
    def update(article: Article) -> None:
        db.session.merge(article)
        db.session.commit()