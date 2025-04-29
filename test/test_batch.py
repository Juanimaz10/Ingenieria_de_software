import os
import unittest
from app import create_app
from app import db
from app.services import BatchService
from utils import new_batch
from datetime import date

class BatchTestCase(unittest.TestCase):

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

    def test_batch(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        self.assertIsNotNone(batch)
        self.assertEqual(batch.code, 'codigo')
        self.assertEqual(batch.expiration_date, date(2025,4,20))

    def test_save(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        batch_save = BatchService.save(batch)
        self.check_data(batch_save)
        batch_delete = BatchService.delete(batch)
        self.assertIsNone(batch_delete)

    def test_find(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        batch_save = BatchService.save(batch)
        self.check_data(batch_save)
        batch = BatchService.find(1)
        self.check_data(batch_save)

    def test_find_all(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        batch2 = new_batch(code="codigo", expiration_date = date(2025,5,20))
        batch2.id = 2
        batch_save = BatchService.save(batch)
        batch2_save = BatchService.save(batch2)
        self.check_data(batch_save)
        self.assertIsNotNone(batch2_save)
        batches = BatchService.find_all()
        self.assertIsNotNone(batches)
        self.assertGreater(len(batches), 1)

    def test_find_by(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        batch_save = BatchService.save(batch)
        self.check_data(batch_save)
        batch = BatchService.find_by(code = 'codigo')
        self.assertIsNotNone(batch)
        self.assertGreater(len(batch), 0)

    def test_update(self):
        batch = new_batch(code="codigo", expiration_date = date(2025,4,20))
        batch_save = BatchService.save(batch)
        batch_save.code = 'new code'
        batch_save_update = BatchService.update(batch_save)
        self.assertEqual(batch_save_update.code, 'new code')
        self.assertEqual(batch_save.code, batch_save_update.code)
        self.assertEqual(batch.code, batch_save_update.code)
    
    def check_data(self, batch_save):
        self.assertIsNotNone(batch_save)
        self.assertIsNotNone(batch_save.id)
        self.assertGreater(batch_save.id, 0)


if __name__ == '__main__':
    unittest.main()