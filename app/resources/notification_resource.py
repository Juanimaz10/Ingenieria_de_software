from flask import jsonify, Blueprint, request
from app.services import NotificationService
from app.mapping import NotificationSchema

# Blueprint para notificaciones
notifications_bp = Blueprint('notifications', __name__)
notification_schema = NotificationSchema()

class NotificationResource:
    def __init__(self, service=None):
        self.service = service or NotificationService()
    
    def handle_exception(self, e, message):
        return jsonify({"error": f"{message}: {str(e)}"}), 500
    
    def get_notification_response(self, notification, success_code=200, not_found_message="Notificación no encontrada"):
        if notification:
            return jsonify({"notification": notification_schema.dump(notification)}), success_code
        return jsonify({"error": not_found_message}), 404
    
    def find_all(self):
        try:
            notifications = self.service.find_all()
            return jsonify({"notifications": notification_schema.dump(notifications, many=True)}), 200
        except Exception as e:
            return self.handle_exception(e, "Error al obtener notificaciones")
    
    def get_by_id(self, notification_id):
        try:
            notification = self.service.find_by_id(notification_id)
            return self.get_notification_response(notification)
        except Exception as e:
            return self.handle_exception(e, "Error al obtener notificación por ID")
    
    def create(self):
        try:
            notification_data = request.json
            notification = notification_schema.load(notification_data)
            return self.get_notification_response(self.service.create(notification))
        except Exception as e:
            return self.handle_exception(e, "Error al agregar notificación")
    
    def delete(self, notification_id):
        try:
            notification = self.service.find_by_id(notification_id)
            return self.get_notification_response(self.service.delete(notification_id))
        except Exception as e:
            return self.handle_exception(e, "Error al eliminar notificación")

# Instancia del controlador
notification_controller = NotificationResource()

# Definición de rutas
notifications_bp.route('/get-all', methods=['GET'])(notification_controller.find_all)
notifications_bp.route('/get/<int:notification_id>', methods=['GET'])(notification_controller.get_by_id)
notifications_bp.route('/add', methods=['POST'])(notification_controller.create)
notifications_bp.route('/delete/<int:notification_id>', methods=['DELETE'])(notification_controller.delete)
