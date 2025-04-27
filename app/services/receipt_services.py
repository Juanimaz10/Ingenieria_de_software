from app import create_app, db  
from app.models import Receipt, ReceiptType  
from app.repositories import ReceiptRepository, ArticleRepository, StockRepository  
from app.dto import ReceiptDTO, ReceiptItemDTO  
from app.models import ReceiptItem, Stock  
from app.repositories.receipt_type_repository import ReceiptTypeRepository  

class ReceiptService:
   

    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':

        ReceiptRepository.save(receipt)
        return receipt

    @staticmethod
    def register_receipt(receipt_dto: ReceiptDTO) -> 'ReceiptDTO':
  
        
        try:
            
            if not receipt_dto.header or not receipt_dto.header.id:
                raise ValueError("ReceiptDTO.header must be a valid and saved ReceiptHeader.")
            if not receipt_dto.Footer or not receipt_dto.Footer.id:
                raise ValueError("ReceiptDTO.Footer must be a valid and saved ReceiptFooter.")

          
            receipt_type = ReceiptTypeRepository.get_by_id(receipt_dto.id_receipt_type)
            if not receipt_type:
                raise ValueError(f"Receipt type with ID {receipt_dto.id_receipt_type} not found.")

           
            receipt = Receipt(
                header=receipt_dto.header.id,
                footer=receipt_dto.Footer.id,
                receipt_type=receipt_dto.id_receipt_type
            )
            ReceiptRepository.save(receipt)

            for item_dto in receipt_dto.items:
            
                article = ArticleRepository.find(item_dto.id_article)
                if not article:
                    raise ValueError(f"Article with ID {item_dto.id_article} not found.")

               
                receipt_item = ReceiptItem(
                    id_article=item_dto.id_article,
                    quantity=item_dto.quantity,
                    batch_id=item_dto.id_batch,
                    receipt_id=receipt.id
                )
                db.session.add(receipt_item)

               
                stock = StockRepository.find_by(article_id=item_dto.id_article, batch_id=item_dto.id_batch)
                if not stock:
                    stock = Stock(article_id=item_dto.id_article, batch_id=item_dto.id_batch, quantity=0)
                    db.session.add(stock)
                stock.quantity += item_dto.quantity
                db.session.merge(stock)

        
            db.session.commit()

            return receipt_dto

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error registering receipt: {str(e)}")

    def setUp(self):
      
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

 
        self.receipt_type = ReceiptType(id=1, name="Factura", description="Factura de venta", type_entry=1)
        db.session.add(self.receipt_type)
        db.session.commit()

        
        assert ReceiptType.query.get(1) is not None, "El tipo de comprobante no se guardó correctamente"

        #TODO: Buscar el tipo de comprobante por id
        #TODO: Buscar el articulo por id de items
        #TODO: Crear un objeto receipt a partir de receipt_dto
        #TODO: Guardar el objeto receipt en la base de datos
        #TODO: Actualizar el stock de los articulos
        #TODO: El guardar y el actualizar deben ser transaccional