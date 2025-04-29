from app.models import Batch

def new_batch(code, expiration_date) -> Batch:
    batch = Batch()
    batch.code = code
    batch.expiration_date = expiration_date
    return batch
