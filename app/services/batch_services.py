from app.models import Batch
from app.repositories import BatchRepository
from typing import List


class BatchService():
    
    def save(batch: Batch) -> 'Batch':

        BatchRepository.save(batch)
        return batch
    
    def delete(batch: 'Batch') -> None:
        BatchRepository.delete(batch)

    def find(id: int) -> 'Batch':
        return BatchRepository.find(id)
    
    def find_all() -> List['Batch']:
        return BatchRepository.find_all()
    
    def find_by(**kwargs) -> List['Batch']:
        return BatchRepository.find_by(**kwargs)
    
    def update(batch: 'Batch') -> 'Batch':
        BatchRepository.update(batch)
        return batch