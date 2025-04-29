import unittest
from datetime import datetime, timezone
import os
from app import create_app, db
from app.models import Notification
from app.services.notification_service import NotificationService
from app.repositories.notification_repository import NotificationRepository

class NotificationTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.repo = NotificationRepository()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_notification(self, type_, message):
        return Notification(type=type_, message=message, date=datetime.now(timezone.utc)) #no repetición de código método, crea instancias de Notification

    # Acá está para models Creación modelo: verificación de guardado y creación en la base de datos.
    def test_model_creation(self):
        notification = self.create_notification('INFO', 'Test message')
        db.session.add(notification)
        db.session.commit()
        saved = Notification.query.first()
        self.assertIsNotNone(saved)
        self.assertEqual(saved.type, 'INFO')
        self.assertEqual(saved.message, 'Test message')

    # Acá esta la parte del test de repo: pruebas del guardado y recuperación. find_all() devuelve 3 notificaciones y find_by() 1 tipo errores 
    # Funciona pero quizá las separe, para que cada método tenga su propia función.
    def test_repo_save_and_find(self):

        notification = self.create_notification('WARNING', 'From repo')
        self.repo.save(notification)
        found = self.repo.find(notification.notification_id)
        self.assertIsNotNone(found)
        self.assertEqual(found.message, 'From repo')

    def test_repo_find_all_and_find_by(self):

        self.repo.save(self.create_notification('INFO', 'One'))
        self.repo.save(self.create_notification('ERROR', 'Two'))
        self.repo.save(self.create_notification('WARNING', 'Three'))
        all_notification = self.repo.find_all()
        self.assertEqual(len(all_notification), 3)
        filtered = self.repo.find_by(type='ERROR')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].type, 'ERROR')

    def test_repo_delete(self):

        notification = self.create_notification('WARNING', 'To delete')
        self.repo.save(notification)
        self.repo.delete(notification)
        self.assertIsNone(self.repo.find(notification.notification_id))

    # Testing parte de service create, find_all, delete 
    def test_service_create_and_find(self): #verifica que create y find funcionen.

        notification = self.create_notification('INFO', 'Service info')
        created = NotificationService.create(notification)
        found = NotificationService.find(created.notification_id)
        self.assertIsNotNone(found)
        self.assertEqual(found.message, 'Service info')

    def test_service_find_all(self): #verifica que retorne las dos notificaciones que se crearon.

        NotificationService.create(self.create_notification('INFO', 'Service 1'))
        NotificationService.create(self.create_notification('ERROR', 'Service 2'))
        all_notifications = NotificationService.find_all()
        self.assertEqual(len(all_notifications), 2)


    def test_service_delete(self): #Guarda la notificación, la elimina con delete(), y luego verifica que find() largue ValueError cuando la busque (en este caso ya no deberia existir).

        notification = self.create_notification('ERROR', 'To be deleted')
        NotificationService.create(notification)
        NotificationService.delete(notification.notification_id)
        with self.assertRaises(ValueError):
            NotificationService.find(notification.notification_id)

if __name__ == '__main__':
    unittest.main()
