import unittest
from flask import current_app
from app import create_app
import os
from app import db
from app.services import BrandService
from utils import new_brand, new_category
brand = new_brand(name='Marca', description='Una Marca')

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
        self.assertIsNotNone(brand)
        self.assertEqual(brand.name, "Marca")
        self.assertEqual(brand.description, "Una Marca")

    def test_save(self):
        brand_save = BrandService.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        
    def test_find(self):
        brand_save = BrandService.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertEqual(brand_save.id, 1)
        brand_find = BrandService.find(brand_save.id)
        self.assertIsNotNone(brand_find)

    def test_find_all(self):
        brand1 = new_brand(name="Marca", description="Una Marca1")
        brand_save = BrandService.save(brand)
        BrandService.save(brand1)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertEqual(brand_save.id, 1)
        brands = BrandService.find_all()
        self.assertIsNotNone(brands)
        self.assertEqual(len(brands), 2)

    def test_find_by_id(self):
        brand_save = BrandService.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        brand_find_by = BrandService.find_by(id = 1)
        self.assertIsNotNone(brand_find_by)

    def test_update(self):
        brand_save = BrandService.save(brand)
        brand_save.name = "Marca Actualizada"
        brand_update_save = BrandService.save(brand_save)
        self.assertEqual(brand_update_save.name, "Marca Actualizada")
        self.assertEqual(brand_save.name, brand_update_save.name)
        self.assertEqual(brand.name, brand_update_save.name)
        
    def test_delete(self):
        brand_save = BrandService.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        product_delete = BrandService.delete(brand_save)
        self.assertIsNone(product_delete)