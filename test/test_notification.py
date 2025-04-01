import unittest
from app import create_app, db
from app.models import Notification
from datetime import datetime, timezone
import os

class NotificationTestCase(unittest.TestCase):
    
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
    
    def test_create_notification(self):
        notification = Notification(type='INFO', message='Test message', date=datetime.now(timezone.utc))
        db.session.add(notification)
        db.session.commit()
        
        saved_notification = Notification.query.first()
        self.assertIsNotNone(saved_notification)
        self.assertEqual(saved_notification.type, 'INFO')
        self.assertEqual(saved_notification.message, 'Test message')

if __name__ == '__main__':
    unittest.main()
