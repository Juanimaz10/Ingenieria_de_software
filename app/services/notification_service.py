from typing import List, Optional
from app.models import Notification
from app.repositories import NotificationRepository

class NotificationService:
    def __init__(self, repository: Optional[NotificationRepository] = None):
        self.repository = repository or NotificationRepository()
    
    def save(self, notification: Notification) -> Notification:
        return self.repository.save(notification)
    
    def delete(self, notification: Notification) -> None:
        self.repository.delete(notification)
    
    def find(self, id: int) -> Optional[Notification]:
        return self.repository.find(id)
    
    def find_all(self) -> List[Notification]:
        return self.repository.find_all()
    
    def find_by(self, **kwargs) -> List[Notification]:
        return self.repository.find_by(**kwargs)
