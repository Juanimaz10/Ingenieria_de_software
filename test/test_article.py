import os
import unittest
from app import create_app
from app import db
from app.models import Article, Category, Brand
from app.services import ArticleService



class ArticleTestCase(unittest.TestCase):
    """
    Test User model
    Necesitamos aplicar principios como DRY( Don't repeat yourself) y KISS (Keep it Simple, Stupid).
    YAGNI (You aren't gonna need it) y SOLID (Single responsability principle).
    """

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_article(self):
        article = self.__new_article()
        self.assertIsNotNone(article)
        self.assertEqual(article.name, 'Tupu')
        self.assertEqual(article.description, 'description')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article = self.__new_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_delete = ArticleService.delete(article)
        self.assertIsNone(article_delete)

    def test_find(self):
        article = self.__new_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article = ArticleService.find(1)
        self.check_data(article_save)

    def test_find_all(self):
        article = self.__new_article()
        article2 = self.__new_article()
        article2.id_article = 2
        article2.category.id = 2
        article2.brand.id = 2
        article_save = ArticleService.save(article)
        article2_save = ArticleService.save(article2)
        self.check_data(article_save)
        self.assertIsNotNone(article2_save)
        articles = ArticleService.find_all()
        self.assertIsNotNone(articles)
        self.assertGreater(len(articles), 1)

    def test_find_by(self):
        article = self.__new_article()
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article = ArticleService.find_by(description = 'description')
        self.assertIsNotNone(article)
        self.assertGreater(len(article), 0)

    def test_update(self):
        article = self.__new_article()
        article_save = ArticleService.save(article)
        article_save.description = 'new description'
        article_save_update = ArticleService.update(article_save)
        self.assertEqual(article_save_update.description, 'new description')
        self.assertEqual(article_save.description, article_save_update.description)
        self.assertEqual(article.description, article_save_update.description)
    
    def __new_category(self):
        category = Category()
        category.id = 1
        category.name = 'Prueba'
        category.description = 'descripcion de prueba'

        return category
    
    def __new_brand(self):
        brand = Brand()
        brand.id = 1
        brand.name = "Marca"
        brand.description = "Una Marca"
        return brand
    
    def __new_article(self):
        article = Article()
        category = self.__new_category()
        brand = self.__new_brand()
        article.id_article = 1
        article.name = 'Tupu'
        article.description = 'description'
        article.category = category
        article.brand = brand
        article.minimun_stock = 1
        article.code_ean13 = 'abc'
        return article


    def check_data(self, article_save):
        self.assertIsNotNone(article_save)
        self.assertIsNotNone(article_save.id_article)
        self.assertGreater(article_save.id_article, 0)


if __name__ == '__main__':
    unittest.main()