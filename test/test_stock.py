import unittest
import os
from app import create_app
from app import db
from app.models import Article, Brand, Category, Stock, Batch
from app.services import StockService
from app.repositories import StockRepository

class TestStock(unittest.TestCase):
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

    def test_stock_creation(self):
        stock = Stock()
        stock.article = Article()

    def test_save(self):
        article = Article(name="Test Article", description="Description", minimun_stock=5, code_ean13="1234567890123")
        batch = Batch(code="Batch001", expiration_date="2025-12-31")

        db.session.add(article)
        db.session.add(batch)
        db.session.commit()

        stock = Stock(article_id=article.id_article, batch_id=batch.id_batch, quantity=10)
        saved_stock = StockService.save(stock)

        self.assertIsNotNone(saved_stock.id)  
        self.assertEqual(saved_stock.quantity, 10)
        self.assertEqual(saved_stock.article.name, "Test Article")
        self.assertEqual(saved_stock.batch.code, "Batch001")
       
if __name__ == '__main__':
    unittest.main()

