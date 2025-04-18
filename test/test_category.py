import os
import unittest
from app import create_app
from app import db
from app.models import Category
from app.services import CategoryService


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
        category = self.__new_category()
        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Prueba')
        self.assertEqual(category.description, 'descripcion de prueba')

    def test_save(self):
        category = self.__new_category()
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category_delete = CategoryService.delete(category)
        self.assertIsNone(category_delete)

    def test_find(self):
        category = self.__new_category()
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category = CategoryService.find(1)
        self.check_data(category_save)

    def test_find_all(self):
        category = self.__new_category()
        category2 = self.__new_category()
        category2.id = 2
        category_save = CategoryService.save(category)
        category2_save = CategoryService.save(category2)
        self.check_data(category_save)
        self.assertIsNotNone(category2_save)
        categories = CategoryService.find_all()
        self.assertIsNotNone(categories)
        self.assertGreater(len(categories), 1)

    def test_find_by(self):
        category = self.__new_category()
        category_save = CategoryService.save(category)
        self.check_data(category_save)
        category = CategoryService.find_by(description = 'descripcion de prueba')
        self.assertIsNotNone(category)
        self.assertGreater(len(category), 0)

    def test_update(self):
        category = self.__new_category()
        category_save = CategoryService.save(category)
        category_save.description = 'new description'
        category_save_update = CategoryService.update(category_save)
        self.assertEqual(category_save_update.description, 'new description')
        self.assertEqual(category_save.description, category_save_update.description)
        self.assertEqual(category.description, category_save_update.description)

    def __new_category(self):
        category = Category()
        category.id = 1
        category.name = 'Prueba'
        category.description = 'descripcion de prueba'

        return category
    
    def check_data(self, category_save):
        self.assertIsNotNone(category_save)
        self.assertIsNotNone(category_save.id)
        self.assertGreater(category_save.id, 0)


if __name__ == '__main__':
    unittest.main()