from app.models import Brand

def new_brand(name, description):
    brand = Brand()
    brand.name = name
    brand.description = description
    return brand
