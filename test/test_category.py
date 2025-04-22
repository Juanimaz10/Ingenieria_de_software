import os
import unittest
from app import create_app
from app import db
from app.services import CategoryService
from utils import new_category
category = new_category(name='Category', description='Una Categoria')

class CategoryTestCase(unittest.TestCase):

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

    def test_category(self):
        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Category')
        self.assertEqual(category.description, 'Una Categoria')

    def test_save(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_delete = CategoryService.delete(category)
        self.assertIsNone(category_delete)

    def test_find(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_find = CategoryService.find(1)
        self.check_data(category_find)

    def test_find_all(self):
        category2 = new_category(name='Category 1', description='Una Categoria 1')
        category_save = CategoryService.save(category)
        category2_save = CategoryService.save(category2)
        self.check_data(category_save)
        self.assertIsNotNone(category2_save)
        categories = CategoryService.find_all()
        self.assertIsNotNone(categories)
        self.assertGreater(len(categories), 1)

    def test_find_by(self):
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_find = CategoryService.find_by(description = 'Una Categoria')
        self.assertIsNotNone(category_find)
        self.assertGreater(len(category_find), 0)

    def test_update(self):
        category_save = CategoryService.save(category)
        category_save.description = 'Una Categoria 2'
        category_save_update = CategoryService.update(category_save)
        self.assertEqual(category_save_update.description, 'Una Categoria 2')
        self.assertEqual(category_save.description, category_save_update.description)
        self.assertEqual(category.description, category_save_update.description)

    def check_data(self, category_save):
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertGreater(category_save.id, 0)

if __name__ == '__main__':
    unittest.main()