from app.models import Receipt
from app.repositories import ReceiptRepository
from app.dto import ReceiptDTO


class ReceiptService:
    """
    Service class for handling receipt-related operations.
    """

    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':
        """
        Save the receipt to the database.
        """
        # Assuming you have a database session object `db_session`
        ReceiptRepository.save(receipt)
        return receipt
    
    @staticmethod
    def register_receipt(receipt_dto: ReceiptDTO) -> 'ReceiptDTO':
        #TODO: Buscar el tipo de comprobante por id
        #TODO: Buscar el articulo por id de items
        #TODO: Crear un objeto receipt a partir de receipt_dto
        #TODO: Guardar el objeto receipt en la base de datos
        #TODO: Actualizar el stock de los articulos
        #TODO: El guardar y el actualizar deben ser transaccionales
        return receipt_dto
    

    
    
