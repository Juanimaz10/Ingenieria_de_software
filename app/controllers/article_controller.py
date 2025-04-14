import logging
from flask import Blueprint, request
from app.services import ArticleService
from app.mapping import ArticleMap
from app.mapping import MessageMap
from app.services import MessageBuilder


article_bp = Blueprint('article', __name__)

@article_bp.route('/article/<int:id>', methods=['GET'])
def get(id:int):
    article = ArticleService.find(id)
    article_map = ArticleMap()
    article_data = article_map.dump(article)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro el articulo').add_data({'article': article_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@article_bp.route('/articles', methods=['GET'])
def get_all():
    articles = ArticleService.find_all()
    article_map = ArticleMap()
    articles_data = article_map.dump(articles, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro todo').add_data({'articles': articles_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@article_bp.route('/articles', methods=['POST'])
def post():
    article_map = ArticleMap()
    article = article_map.load(request.json)
    ArticleService.save(article)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Articulo creado').build()
    return message_map.dump(message_finish), 200


@article_bp.route('/articles/<int:id>', methods=['PUT'])
def put(id:int):
    article_map = ArticleMap()
    new_article = article_map.load(request.json)
    ArticleService.update(new_article)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Articulo actualizado').build()
    return message_map.dump(message_finish), 200

@article_bp.route('/articles/<int:id>', methods=['DELETE'])
def delete(id:int):
    article = ArticleService.find(id)
    ArticleService.delete(article)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(f'Se elimino el articulo {id}').build()
    return message_map.dump(message_finish), 200