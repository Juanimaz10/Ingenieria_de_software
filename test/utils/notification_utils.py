from app.models import Notification

def new_notification(type, message, date) -> Notification:
    notification = Notification()
    type.type = type
    message.message = message
    date.date = date
    return notification