import unittest
from flask import current_app
from app import create_app
from app.models import Category
import os

class CategoryTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_new_category(self):
        category = Category('notebook', 'notebook gamer')
        self.assertIsNotNone(category)

if __name__ == '__main__':
    unittest.main()