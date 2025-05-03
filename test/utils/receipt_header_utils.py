import datetime
from app.models import ReceiptHeader

def new_receipt_header(submission_date: datetime) -> ReceiptHeader:
    header = ReceiptHeader()
    header.submission_date = submission_date
    return header