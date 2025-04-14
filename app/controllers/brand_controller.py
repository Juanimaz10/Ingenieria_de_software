import logging
from flask import Blueprint, request
from app.mapping import MessageMap, BrandMap
from app.services import MessageBuilder, BrandService

brand_bp = Blueprint('brand', __name__)
brand_map = BrandMap()
brand_service = BrandService()

result = {}
status_code = 200

@brand_bp.route('/brand/<int:id>', methods=['GET'])
def get(id: int):
    """Get a brand by ID."""
    logging.debug(f"Request to get brand with ID: {id}")
    brand = brand_service.find(id)
    message_map, message_finish = message_create(brand_map.dump(brand, many=False), "Se encontro la marca indicada")
    result = message_map.dump(message_finish)
    return result, status_code


@brand_bp.route('/brand', methods=['GET'])
def get_all():
    """Get all brands."""
    logging.debug("Request to get all brands")
    brands = brand_service.find_all()
    message_map, message_finish = message_create({'brands': brand_map.dump(brands, many=True)}, "Se encontraron todas las marcas")
    result = message_map.dump(message_finish)
    return result, status_code

@brand_bp.route('/brand', methods=['POST'])
def post():
    """Create a new brand."""
    logging.debug("Request to create a new brand")
    brand = brand_map.load(request.json)
    brand_service.save(brand)
    message_map, message_finish = message_create(brand_map.dump(brand), "Marca creada con éxito")
    result = message_map.dump(message_finish)
    status_code = 201
    return result, status_code

@brand_bp.route('/brand/<int:id>', methods=['PUT'])
def update(id: int):
    """Update a brand by ID."""
    logging.debug(f"Request to update brand with ID: {id}")
    brand = brand_service.find(id)
    if not brand:
        message_map, message_finish = message_create({}, "Marca no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        updated_data = request.json
        for key, value in updated_data.items():
            setattr(brand, key, value)
        updated_brand = brand_service.save(brand)
        message_map, message_finish = message_create(brand_map.dump(updated_brand), "Marca actualizada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code

@brand_bp.route('/brand/<int:id>', methods=['DELETE'])
def delete(id: int):
    """Delete a brand by ID."""
    logging.debug(f"Request to delete brand with ID: {id}")
    brand = brand_service.find(id)
    if not brand:
        message_map, message_finish = message_create({}, "Marca no encontrada")
        result = message_map.dump(message_finish)
        status_code = 404
    else:
        brand_service.delete(brand)
        message_map, message_finish = message_create({}, "Marca eliminada con éxito")
        result = message_map.dump(message_finish)
        status_code = 200
    return result, status_code


def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map, message_finish