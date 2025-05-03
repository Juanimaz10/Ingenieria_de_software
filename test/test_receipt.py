import os
import unittest
from app import db, create_app
from app.models import article, batch
from app.models.receipt import Receipt
from app.models.receipt_footers import ReceiptFooter
from app.models.receipt_header import ReceiptHeader
from app.models.receipt_items import ReceiptItem
from app.models.receipt_types import ReceiptType
from app.services.article_service import ArticleService
from app.services.batch_service import BatchService
from app.services.brand_service import BrandService
from app.services.category_service import CategoryService
from app.services.receipt_footer_service import ReceiptFooterService
from app.services.receipt_header_service import ReceiptHeaderService
from app.services.receipt_type_service import ReceiptTypesService
from utils import new_receipt, new_receipt_type, new_brand, new_article, new_batch, new_receipt_items, new_category, new_receipt_footer, new_receipt_header
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
    """Test que verifica guardar un receipt completo"""
    
    brand = new_brand(name="brand", description="brand")
    BrandService.save(brand)
    
    category = new_category(name="category_name", description="description")
    CategoryService.save(category)
    
    article = new_article(
        name="name", 
        description="article", 
        brand=brand,
        category=category,
        minimun_stock=10, 
        code_ean13="1234567890123"
    )
    ArticleService.save(article)
    
    batch = new_batch(code="LOTE123", expiration_date=datetime.now())
    BatchService.save(batch)
    
    receipt_type = new_receipt_type(
        name="remito de entrada", 
        description="remito de entrada", 
        type_entry=1
    )
    ReceiptTypesService.save(receipt_type)
    
    header = new_receipt_header(submission_date=datetime.now())
    ReceiptHeaderService.save(header)
    
    footer = new_receipt_footer(total=100.0)
    ReceiptFooterService.save(footer)
    
    receipt = new_receipt(
        receipt_type=receipt_type,
        id_header=header.id,
        id_footer=footer.id
    )
    
    receipt_item = new_receipt_items(
        article=article,
        batch=batch,
        quantity=10,
        receipt=receipt
    )
    
    if not hasattr(receipt, 'items'):
        receipt.items = []
    receipt.items.append(receipt_item)
    
    ReceiptService.save(receipt)
    
    saved_receipt = Receipt.query.get(receipt.id)
    self.assertIsNotNone(saved_receipt)
    self.assertEqual(len(saved_receipt.items), 1)
    self.assertEqual(saved_receipt.items[0].article.id, article.id)
    self.assertEqual(saved_receipt.items[0].batch.id, batch.id)

        

    
if __name__ == '__main__':
    unittest.main()