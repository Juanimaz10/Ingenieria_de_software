from dataclasses import dataclass

@dataclass(init=True)
class Category():
    name: str
    description: str

