from typing import List
from app.models import Batch
from app import db


class BatchRepository():
    
    def save(batch: Batch) -> 'Batch':
        db.session.add(batch)
        db.session.commit()
        return batch
    
    def delete(batch: Batch) -> None:
        db.session.delete(batch)
        db.session.commit()

    def find(id: int) -> 'Batch':
        return Batch.query.get(id)
    
    def find_all() -> List[Batch]:
        return Batch.query.all()
    
    def find_by(**kwargs) -> List[Batch]:
        return Batch.query.filter_by(**kwargs).all()
    
    def update(batch: Batch) -> None:
        db.session.merge(batch)
        db.session.commit()