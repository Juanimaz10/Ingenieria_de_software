from app.models import Article
from app.repositories import ArticleRepository
from typing import List


class ArticleService():
    
    def save(article: Article) -> 'Article':

        ArticleRepository.save(article)
        return article
    
    def delete(article: 'Article') -> None:
        ArticleRepository.delete(article)

    def find(id: int) -> 'Article':
        return ArticleRepository.find(id)
    
    def find_all() -> List['Article']:
        return ArticleRepository.find_all()
    
    def find_by(**kwargs) -> List['Article']:
        return ArticleRepository.find_by(**kwargs)
    
    def update(article: 'Article') -> 'Article':
        ArticleRepository.update(article)
        return article