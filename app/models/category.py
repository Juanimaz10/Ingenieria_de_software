from dataclasses import dataclass
from app import db


@dataclass(init=True, eq=True)
class Category(db.Model):
    __tablename__ = "category"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column("name", db.String(100), nullable=False)
    description: str = db.Column("description", db.String(250), nullable=False)

    def __eq__(self, category: object) -> bool:
        return (self.id == category.id)

