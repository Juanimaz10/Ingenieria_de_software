from typing import List
from app.models import Notification
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class NotificationRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):
    
    def save(self, notification: Notification) -> Notification:
        db.session.add(notification)
        db.session.commit()
        return notification
    
    def delete(self, notification: Notification) -> None:
        db.session.delete(notification)
        db.session.commit()
    
    def find(self, id: int) -> 'Notification':
        return Notification.query.get(id)

    def find_all(self) -> List['Notification']:
        return Notification.query.all()
    
    def find_by(self, **kwargs) -> List['Notification']:
        return Notification.query.filter_by(**kwargs).all()
