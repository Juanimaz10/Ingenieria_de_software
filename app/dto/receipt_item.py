from dataclasses import dataclass


@dataclass
class ReceiptItemDTO:
    id_article: int
    quantity: int
    id_batch: int
