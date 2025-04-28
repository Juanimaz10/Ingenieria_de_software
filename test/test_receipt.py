from datetime import datetime
import os
import unittest
from app import create_app
from app import db
from app.models import Receipt, ReceiptFooter, ReceiptHeader, ReceiptItem, ReceiptType
from app.services import ReceiptService




class ReceiptTestCase(unittest.TestCase):
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
    
    def test_receipt_creation(self):
        receipt = Receipt()
        
        header = self.__get_header()
        items = self.__get_items()
        footer = self.__get_footer()
        receipt.header = header
        receipt.items = items
        receipt.footer = footer
        self.assertEqual(receipt.header.id, header.id)
        self.assertEqual(receipt.footer.id, footer.id)
        self.assertEqual(len(receipt.items), len(items))
    
    def test_receipt_save(self):
        # Crear y guardar el header
        header = self.__get_header()
        db.session.add(header)
        db.session.commit()

        # Crear y guardar el footer
        footer = self.__get_footer()
        db.session.add(footer)
        db.session.commit()

        # Crear y guardar los items
        items = self.__get_items()
        for item in items:
            db.session.add(item)
        db.session.commit()

        # Crear el receipt y asignar los IDs
        receipt = Receipt()
        receipt.header = header.id  # Asignar el ID del header
        receipt.footer = footer.id  # Asignar el ID del footer

        # Guardar el receipt
        db.session.add(receipt)
        db.session.commit()

        # Verificar que el receipt tenga un ID asignado
        self.assertIsNotNone(receipt.id)
    

    def __get_header(self) -> ReceiptHeader:
        header = ReceiptHeader() 
        header.id = 1
        header.submission_date = datetime.now()
        return header


    def __get_items(self) -> list[ReceiptItem]:
        items = []
        items.append(ReceiptItem(id=1, id_article=1, quantity=2.0, batch='batch1')) 
        items.append(ReceiptItem(id=2, id_article=2, quantity=3.0, batch='batch2'))
        items.append(ReceiptItem(id=3, id_article=3, quantity=4.0, batch='batch3'))
        return items
    
    def __get_footer(self) -> ReceiptFooter:
        footer = ReceiptFooter()
        footer.id = 1
        footer.total = 100.0
        return footer
    