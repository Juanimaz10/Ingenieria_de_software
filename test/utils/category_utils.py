from app.models import Category

def new_category(name, description) -> Category:
    category = Category()
    category.name = name
    category.description = description
    return category

