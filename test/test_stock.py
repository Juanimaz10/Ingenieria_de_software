import unittest
import os
from app import create_app
from app import db
from app.models import Article, Brand, Category,Stock


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

   
    
if __name__ == '__main__':
    unittest.main()

