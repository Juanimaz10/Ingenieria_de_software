from app.models import Article
from app.repositories import ArticleRepository
from typing import List


class ArticleService():
    
    @staticmethod
    def save(article: Article) -> 'Article':
        ArticleRepository.save(article)
        return article
    
    @staticmethod
    def delete(article: 'Article') -> None:
        ArticleRepository.delete(article)
    
    @staticmethod
    def find(id: int) -> 'Article':
        return ArticleRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Article']:
        return ArticleRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Article']:
        return ArticleRepository.find_by(**kwargs)
    
    @staticmethod
    def update(article: 'Article') -> 'Article':
        ArticleRepository.update(article)
        return article