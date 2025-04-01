from dataclasses import dataclass
from app import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

@dataclass
class Notification(db.Model):
    __tablename__ = 'notifications'
    
    notification_id: int = Column(Integer, primary_key=True, autoincrement=True)
    type: str = Column(String(20), nullable=False)  # INFO, WARNING, ERROR
    message: str = Column(String(255), nullable=False)
    date: datetime = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

