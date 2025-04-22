import os
import unittest
from app import create_app
from app import db
from app.services import ArticleService
from utils import new_article, new_brand, new_category
brand = new_brand(name='Marca', description='Una Marca')
category = new_category(name='Category', description='Una Categoria')
article = new_article(name='Tupu', description='description', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')

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
        self.assertIsNotNone(article)
        self.assertEqual(article.name, 'Tupu')
        self.assertEqual(article.description, 'description')
        self.assertEqual(article.minimun_stock, 1)
        self.assertEqual(article.code_ean13, 'abc')

    def test_save(self):
        article_save = ArticleService.save(article)
        self.check_data(article_save)

    def test_find(self):
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_find = ArticleService.find(article_save.id_article)
        self.check_data(article_find)

    def test_find_all(self):
        article2 = new_article(name='Tupu2', description='description2', category=category.id, brand=brand.id, minimun_stock=1, code_ean13='abc')
        article_save = ArticleService.save(article)
        article2_save = ArticleService.save(article2)
        self.check_data(article_save)
        self.assertIsNotNone(article2_save)
        articles = ArticleService.find_all()
        self.assertIsNotNone(articles)
        self.assertGreater(len(articles), 1)

    def test_find_by(self):
        article_save = ArticleService.save(article)
        self.check_data(article_save)
        article_save = ArticleService.find_by(description = 'description')
        self.assertIsNotNone(article_save)
        self.assertGreater(len(article_save), 0)

    def test_update(self):
        article_save = ArticleService.save(article)
        article_save.description = 'new description'
        article_save_update = ArticleService.update(article_save)
        self.assertEqual(article_save_update.description, 'new description')
        self.assertEqual(article_save.description, article_save_update.description)
        self.assertEqual(article.description, article_save_update.description)

    def check_data(self, article_save):
        self.assertIsNotNone(article_save)
        self.assertIsNotNone(article_save.id_article)
        self.assertGreater(article_save.id_article, 0)


if __name__ == '__main__':
    unittest.main()