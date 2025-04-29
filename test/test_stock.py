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

    

if __name__ == '__main__':
    unittest.main()
       