import logging
from flask import Blueprint, request
from app.services import CategoryService
from app.mapping import CategoryMap
from app.mapping import MessageMap
from app.services import MessageBuilder


category_bp = Blueprint('category', __name__)

@category_bp.route('/category/<int:id>', methods=['GET'])
def get(id:int):
    category = CategoryService.find(id)
    category_map = CategoryMap()
    category_data = category_map.dump(category)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro la categoria').add_data({'category': category_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@category_bp.route('/categories', methods=['GET'])
def get_all():
    categories = CategoryService.find_all()
    category_map = CategoryMap()
    categories_data = category_map.dump(categories, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro todo').add_data({'categories': categories_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@category_bp.route('/categories', methods=['POST'])
def post():
    category_map = CategoryMap()
    category = category_map.load(request.json)
    CategoryService.save(category)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Categoria creada').build()
    return message_map.dump(message_finish), 200


@category_bp.route('/categories/<int:id>', methods=['PUT'])
def put(id:int):
    category_map = CategoryMap()
    new_category = category_map.load(request.json)
    CategoryService.update(new_category)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Categoria actualizada').build()
    return message_map.dump(message_finish), 200

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete(id:int):
    category = CategoryService.find(id)
    CategoryService.delete(category)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(f'Se elimino la categoria {id}').build()
    return message_map.dump(message_finish), 200