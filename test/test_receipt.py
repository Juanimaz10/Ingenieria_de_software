from os import name
import unittest
from app.models.receipt_footers import ReceiptFooter
from app.services.receipt_service import ReceiptService
from app.dto import ReceiptDTO
from app.models.receipt_types import ReceiptType
from app import db, create_app
from app.models import ReceiptHeader
from datetime import datetime

class TestReceiptService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

       
        self.receipt_type = ReceiptType(id=1, name="Factura", description="Factura de venta", type_entry=1)
        db.session.add(self.receipt_type)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    
if __name__ == '__main__':
    unittest.main()