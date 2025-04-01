import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.models import Brand
from app.services import BrandService
service = BrandService()

class BrandTestCase(unittest.TestCase):

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
    
    def test_brand(self):
        brand = self.__new_brand()
        self.assertIsNotNone(brand)
        self.assertEqual(brand.name, "Marca")
        self.assertEqual(brand.description, "Una Marca")

    def test_save(self):
        brand = self.__new_brand()
        brand_save = service.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        
    def test_find(self):
        brand = self.__new_brand()
        brand_save = service.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertEqual(brand_save.id, 1)
        brand_find = service.find(brand_save.id)
        self.assertIsNotNone(brand_find)

    def test_find_all(self):
        brand = self.__new_brand()
        brand1 = self.__new_brand()
        brand1.name = "Marca 1"
        brand1.description = "Una Marca 1"
        brand_save = service.save(brand)
        service.save(brand1)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertEqual(brand_save.id, 1)
        brands = service.find_all()
        self.assertIsNotNone(brands)
        self.assertEqual(len(brands), 2)

    def test_find_by_id(self):
        brand = self.__new_brand()
        brand_save = service.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        brand_find_by = service.find_by(id = 1)
        self.assertIsNotNone(brand_find_by)

    def test_update(self):
        brand = self.__new_brand()
        brand_save = service.save(brand)
        brand_save.name = "Marca Actualizada"
        brand_update_save = service.save(brand_save)
        self.assertEqual(brand_update_save.name, "Marca Actualizada")
        self.assertEqual(brand_save.name, brand_update_save.name)
        self.assertEqual(brand.name, brand_update_save.name)
        

    def test_delete(self):
        brand = self.__new_brand()
        brand_save = service.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        product_delete = service.delete(brand_save)
        self.assertIsNone(product_delete)


    def __new_brand(self):
        brand = Brand()
        brand.name = "Marca"
        brand.description = "Una Marca"
        return brand