from abc import ABC, abstractmethod
from typing import List
from app import db

class CreateAbstractRepository(ABC):

    @abstractmethod
    def save(self, model:db.Model) -> db.Model:
        pass

class ReadAbstractRepository(ABC):
    
    @abstractmethod
    def find(self, id: int) -> 'db.Model':
        pass

    @abstractmethod
    def find_all(self) -> List['db.Model']:
        pass
    
    @abstractmethod
    def find_by(self, **kwargs) -> List['db.Model']:
        pass

class UpdateAbstractRepository(ABC):

    @abstractmethod
    def update(self, id: int, model:db.Model) -> db.Model:
        pass

class DeleteAbstractRepository(ABC):
    
    @abstractmethod
    def delete(self, model:db.Model) -> None:
        pass