import unittest
from app import create_app
import os
from app import db
from app.services import StockService
from utils import new_stock, new_article, new_batch, new_receipt


class StockTestCase(unittest.TestCase):

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

    def test_stock(self):
        article = new_article(name="Test Article", code="TEST001", price=10.0, stock=10)
        quantity = 10
        batch = new_batch(code="BATCH001", expiration_date="2023-12-31")
        receipt = new_receipt(id_header=1, id_footer=1, id_receipt_type=1)
        stock = new_stock(article=article, quantity=quantity, batch=batch, receipt=receipt)
        self.assertIsNotNone(stock)
        self.assertEqual(stock.quantity, 10)
        self.assertEqual(stock.batch_id, 1)
        self.assertEqual(stock.article_id, 1)
        self.asssertEaqual(stock.receipt_id,1)

    def test_save(self):
        stock = new_stock(quantity=10, batch_id=1, article_id=1, receipt_id=1)
        self.assertIsNotNone(stock)
        stock_save = StockService.save(stock)
        self.assertIsNotNone(stock_save)
        self.assertIsNotNone(stock_save.id)
        self.assertGreater(stock_save.id, 0)
        self.assertEqual(stock_save.quantity, 10)
        self.assertEqual(stock_save.batch_id, 1)
        self.assertEqual(stock_save.article_id, 1)
        self.assertEqual(stock_save.receipt_id, 1)

    def test_register(self):
        stock = new_stock(quantity=10, batch_id=1, article_id=1, receipt_id=1)
        self.assertIsNotNone(stock)
        stock_save = StockService.register(stock)
        self.assertIsNotNone(stock_save)
        self.assertIsNotNone(stock_save.id)
        self.assertGreater(stock_save.id, 0)
        self.assertEqual(stock_save.quantity, 10)
        self.assertEqual(stock_save.batch_id, 1)
        self.assertEqual(stock_save.article_id, 1)
        self.assertEqual(stock_save.receipt_id, 1)

    def test_find(self):
        stock = new_stock(quantity=10, batch_id=1, article_id=1, receipt_id=1)
        self.assertIsNotNone(stock)
        stock_save = StockService.save(stock)
        self.assertIsNotNone(stock_save)
        self.assertIsNotNone(stock_save.id)
        self.assertEqual(stock_save.id, 1)
        stock_find = StockService.find(stock_save.id)
        self.assertIsNotNone(stock_find)

    def test_find_all(self):
        stock = new_stock(quantity=10, batch_id=1, article_id=1)
        stock1 = new_stock(quantity=20, batch_id=2, article_id=2)
        stock_save = StockService.save(stock)
        StockService.save(stock1)
        self.assertIsNotNone(stock_save)
        self.assertIsNotNone(stock_save.id)
        self.assertEqual(stock_save.id, 1)
        stocks = StockService.find_all()
        self.assertIsNotNone(stocks)
        self.assertEqual(len(stocks), 2)

    def test_find_by_id(self):
        stock = new_stock(quantity=10, batch_id=1, article_id=1)
        stock_save = StockService.save(stock)
        self.assertIsNotNone(stock_save)
        self.assertIsNotNone(stock_save.id)
        self.assertEqual(stock_save.id, 1)
        stock_find = StockService.find(stock_save.id)
        self.assertIsNotNone(stock_find)

if __name__ == '__main__':
    unittest.main()
       