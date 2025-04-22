from app.models import Article

def new_article(name, description, category, brand, minimun_stock, code_ean13) -> Article:
    article = Article()
    article.name = name
    article.description = description
    article.category = category
    article.brand = brand
    article.minimun_stock = minimun_stock
    article.code_ean13 = code_ean13
    return article
