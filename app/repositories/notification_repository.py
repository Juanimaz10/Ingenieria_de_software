from typing import List
from app.models import Notification
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class NotificationRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):
    
    @staticmethod
    def save(notification: Notification) -> Notification:
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def delete(notification: Notification) -> None:
        db.session.delete(notification)
        db.session.commit()
    
    @staticmethod
    def find(id: int) -> 'Notification':
        return Notification.query.get(id)

    @staticmethod
    def find_all() -> List['Notification']:
        return Notification.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Notification']:
        return Notification.query.filter_by(**kwargs).all()
