import unittest
import os
from app import create_app, db
from app.models import Article, Batch, Stock
from app.services import StockService

class TestStock(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Predefined data for tests
        self.article = Article(name="Test Article", description="Description", minimun_stock=5, code_ean13="1234567890123")
        self.batch = Batch(code="Batch001", expiration_date="2025-12-31")
        db.session.add(self.article)
        db.session.add(self.batch)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_stock_creation(self):
    # Verifica que los datos de Article y Batch existen
        self.assertIsNotNone(self.article.id)
        self.assertIsNotNone(self.batch.id)

    # Crea un objeto Stock
        stock = Stock(article_id=self.article.id, batch_id=self.batch.id, quantity=10)
        self.assertEqual(stock.article_id, self.article.id)
        self.assertEqual(stock.batch_id, self.batch.id)
        self.assertEqual(stock.quantity, 10)

def test_save_stock(self):
    # Crea y guarda un objeto Stock
    stock = Stock(article_id=self.article.id, batch_id=self.batch.id, quantity=10)
    saved_stock = StockService.save(stock)

    # Verifica que el Stock se guardó correctamente
    self.assertIsNotNone(saved_stock.id)
    self.assertEqual(saved_stock.quantity, 10)
    self.assertEqual(saved_stock.article.name, "Test Article")
    self.assertEqual(saved_stock.batch.code, "Batch001")

if __name__ == '__main__':
    unittest.main()