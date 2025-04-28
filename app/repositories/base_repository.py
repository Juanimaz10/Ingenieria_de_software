from abc import ABC, abstractmethod
from typing import List
from app import db

class CreateAbstractRepository(ABC):

    @abstractmethod
    def save(model:db.Model) -> db.Model:
        pass

class ReadAbstractRepository(ABC):
    
    @abstractmethod
    def find(id: int) -> 'db.Model':
        pass

    @abstractmethod
    def find_all() -> List['db.Model']:
        pass
    
    @abstractmethod
    def find_by(**kwargs) -> List['db.Model']:
        pass

class UpdateAbstractRepository(ABC):

    @abstractmethod
    def update(id: int, model:db.Model) -> db.Model:
        pass

class DeleteAbstractRepository(ABC):
    
    @abstractmethod
    def delete(model:db.Model) -> None:
        pass