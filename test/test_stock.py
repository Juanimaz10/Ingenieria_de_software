import unittest
from stock import Stock
from app.models import db
from app.models import Article

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

