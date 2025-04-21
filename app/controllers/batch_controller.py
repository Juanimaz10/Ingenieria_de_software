import logging
from flask import Blueprint, request
from app.services import BatchService
from app.mapping import BatchMap
from app.mapping import MessageMap
from app.services import MessageBuilder


batch_bp = Blueprint('batch', __name__)

@batch_bp.route('/batch/<int:id>', methods=['GET'])
def get(id:int):
    batch = BatchService.find(id)
    batch_map = BatchMap()
    batch_data = batch_map.dump(batch)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro el Lote').add_data({'batch': batch_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@batch_bp.route('/batches', methods=['GET'])
def get_all(): 
    batches = BatchService.find_all()
    batch_map = BatchMap()
    batches_data = batch_map.dump(batches, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontro todo').add_data({'batches': batches_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@batch_bp.route('/batches', methods=['POST'])
def post():
    batch_map = BatchMap()
    batch = batch_map.load(request.json)
    BatchService.save(batch)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Lote creado').build()
    return message_map.dump(message_finish), 200


@batch_bp.route('/batches/<int:id>', methods=['PUT'])
def put(id:int):
    batch_map = BatchMap()
    new_batch = batch_map.load(request.json)
    BatchService.update(new_batch)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Lote actualizado').build()
    return message_map.dump(message_finish), 200

@batch_bp.route('/batches/<int:id>', methods=['DELETE'])
def delete(id:int):
    batch = BatchService.find(id)
    BatchService.delete(batch)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(f'Se elimino el Lote {id}').build()
    return message_map.dump(message_finish), 200