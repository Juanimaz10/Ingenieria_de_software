from datetime import datetime
import random
import unittest
from app import create_app
import os
from app import db
from app.services import StockService, ArticleService, BatchService, BrandService, CategoryService, ReceiptService, ReceiptFooterService, ReceiptHeaderService, ReceiptTypesService
from utils import new_stock, new_article, new_brand, new_category, new_batch, new_receipt, new_receipt_type, new_receipt_footer, new_receipt_header, new_receipt_items

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
        category = new_category(name='Category', description='Una Categoria')
        brand = new_brand(name='Marca', description='Una Marca')
        article = new_article(name='Tupu', description='description', category=category, brand=brand, minimun_stock=1, code_ean13='abc')
        batch = new_batch(code="codigo", expiration_date = datetime.now())
        receipt_type = new_receipt_type(name = "remito de entrada", description = "remito de entrada", type_entry = 1)
        receipt = new_receipt(id_footer=1, id_header=1, receipt_type=receipt_type)
        stock = new_stock(article=article, batch=batch, receipt=receipt, quantity=10)
        self.assertIsNotNone(stock)

    def test_register(self):
        category = new_category(name='Category', description='Una Categoria')
        CategoryService.save(category)

        brand = new_brand(name='Marca', description='Una Marca')
        BrandService.save(brand)

        articles = [
            new_article(name='Teclado', description='Teclado mecánico', category=category, brand=brand, minimun_stock=1, code_ean13='1111111111111'),
            new_article(name='Mouse', description='Mouse inalámbrico', category=category, brand=brand, minimun_stock=1, code_ean13='2222222222222'),
            new_article(name='Monitor', description='Monitor 24 pulgadas', category=category, brand=brand, minimun_stock=1, code_ean13='3333333333333'),
        ]
        for article in articles:
            ArticleService.save(article)
        
        batch = new_batch(code="codigo", expiration_date = datetime.now())
        BatchService.save(batch)
        
        receipt_type_entry = new_receipt_type(name="Entrada", description="Entrada de stock", type_entry=1)
        receipt_type_exit = new_receipt_type(name="Salida", description="Salida de stock", type_entry=-1)
        ReceiptTypesService.save(receipt_type_entry)
        ReceiptTypesService.save(receipt_type_exit)
        
        header = new_receipt_header(submission_date=datetime.now())
        ReceiptHeaderService.save(header)
        
        footer = new_receipt_footer(total=100.0)
        ReceiptFooterService.save(footer)
    
        receipts_data = [
            {"type": receipt_type_entry, "description": "Entrada 1"},
            {"type": receipt_type_exit, "description": "Salida 1"},
            {"type": receipt_type_entry, "description": "Entrada 2"},
        ]

        initial_stock = {}

        for index, receipt_data in enumerate(receipts_data):
            receipt = new_receipt(receipt_type=receipt_data["type"], id_header=header.id, id_footer=footer.id)

            quantities = [random.randint(1, 20) for _ in articles]

            for article, quantity in zip(articles, quantities):
                receipt_item = new_receipt_items(article=article, batch=batch, quantity=quantity, receipt=receipt)
                if not hasattr(receipt, 'items'):
                    receipt.items = []
                receipt.items.append(receipt_item)

                if index == 0:
                    initial_stock[article.id] = quantity
                    stock = new_stock(article=article, batch=batch, receipt=receipt, quantity=quantity)
                    StockService.register(stock)

            if index == 0:
                ReceiptService.save(receipt)
                continue

            for article, quantity in zip(articles, quantities):
                current_stock = StockService.calculate_stock(article.id)
                adjusted_stock = current_stock + (quantity * receipt_data["type"].type_entry)

                if adjusted_stock < 0:
                    print(f"No es posible restar {quantity} del artículo {article.name}. El stock resultante sería negativo.")
                    continue

                stock = new_stock(article=article, batch=batch, receipt=receipt, quantity=adjusted_stock)
                saved_stock = StockService.register(stock)

                self.assertIsNotNone(saved_stock)
            ReceiptService.save(receipt)

if __name__ == '__main__':
    unittest.main()
       