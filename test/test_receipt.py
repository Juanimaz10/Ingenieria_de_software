from os import name
import os
import unittest
from app import db, create_app
from utils import new_receipt, new_receipt_type, new_brand, new_article, new_batch, new_receipt_items
from app.services import ReceiptService
from datetime import datetime

class TestReceiptService(unittest.TestCase):
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
    
    def test_receipt(self):
        receipt_type = new_receipt_type(name = "remito de entrada", description = "remito de entrada", type_entry = 1)
        receipt = new_receipt(id_footer=1, id_header=1, receipt_type=receipt_type)
        self.assertIsNotNone(receipt)

    def test_save_receipt(self):
        brand = new_brand(name = "brand", description = "brand")
        article = new_article(name = "name", description = "article", brand = brand, category = new_category, minimun_stock = 10, code_ean13 = "1234567890123")
        batch = new_batch(article = article, quantity = 10, expiration_date = datetime.now(), items = 10)
        receipt_items = new_receipt_items(article = article, batch = batch, quantity = 10, receipt = receipt)
        receipt_type = new_receipt_type(name = "remito de entrada", description = "remito de entrada", type_entry = 1)
        receipt = new_receipt(id_footer=1, id_header=1, receipt_type=receipt_type)
        receipt.items.append(receipt_items)
        ReceiptService.save(receipt)
        self.assertIsNotNone(receipt)
    

        

    
if __name__ == '__main__':
    unittest.main()