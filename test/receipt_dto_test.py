from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.dto import ReceiptDTO, ReceiptItemDTO
from app.models import ReceiptHeader, ReceiptFooter



class ReceiptDtoCase(unittest.TestCase):
    """
    Receipt Mode
    Necesitamos aplicar principios como DRY( Don't repeat yourself) y KISS (Keep it Simple, Stupid).
    YAGNI (You aren't gonna need it) y SOLID (Single responsability principle).
    """

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
    
    def test_receipt_dto_creation(self):
        receiptdto = ReceiptDTO()
        header = self.__get_header()
        items = self.__get_items()
        footer = self.__get_footer()
        receiptdto.header = header
        receiptdto.items = items
        receiptdto.footer = footer
        header.id_receipt_type = 1
        self.assertIsNotNone(receiptdto)

    def __get_header(self) -> ReceiptHeader:
        header = ReceiptHeader() 
        header.id = 1
        header.submission_date = datetime.now()
        return header


    def __get_items(self) -> list[ReceiptItemDTO]:
        items = []
        items.append(ReceiptItemDTO(id_article=1, quantity=2.0, batch_id= 1)) 
        items.append(ReceiptItemDTO(id_article=2, quantity=3.0, batch_id= 2))
        items.append(ReceiptItemDTO(id_article=3, quantity=4.0, batch_id= 3))
        return items
    
    def __get_footer(self) -> ReceiptFooter:
        footer = ReceiptFooter()
        footer.id = 1
        footer.total = 100.0
        return footer
    