from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class Brand(db.Model):
    __tablename__ = "brands"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column("name", db.String(100), nullable=False)
    description: str = db.Column("description", db.String(250), nullable=False)
    
    def __eq__(self, brand: object) -> bool:
        return (self.id == brand.id)