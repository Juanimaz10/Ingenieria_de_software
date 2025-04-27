from os import name
import unittest
from app.models.receipt_footers import ReceiptFooter
from app.services.receipt_services import ReceiptService
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

    def test_register_receipt_success(self):
        receipt_header = ReceiptHeader(submission_date=datetime.now())
        db.session.add(receipt_header)
        db.session.commit()

    
        receipt_footer = ReceiptFooter(total=100.0)
        db.session.add(receipt_footer)
        db.session.commit()

       
        receipt_dto = ReceiptDTO(
            header=receipt_header,  
            items=[],
            Footer=receipt_footer, 
            id_receipt_type=self.receipt_type.id
        )

        
        result = ReceiptService.register_receipt(receipt_dto)

      
        self.assertIsNotNone(result)
        self.assertEqual(result.header.id, receipt_header.id)
        self.assertEqual(result.Footer.id, receipt_footer.id)
        self.assertEqual(result.id_receipt_type, self.receipt_type.id)

    def test_register_receipt_with_invalid_receipt_type(self):
        receipt_dto = ReceiptDTO(header=None, items=[], Footer=None, id_receipt_type=999)
        with self.assertRaises(ValueError):
            ReceiptService.register_receipt(receipt_dto)

if name == 'main':
    unittest.main()