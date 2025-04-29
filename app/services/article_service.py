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
        article_service = ArticleRepository.find(id)
        if not article_service:
                    raise ValueError(f"Article with ID {id} not found.")
        return article_service
    
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