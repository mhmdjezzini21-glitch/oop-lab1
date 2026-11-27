from src.models.orders import Order
from src.models.warehouse import Warehouse
from src.exceptions import InsufficientStockException

class InventoryService:
    """Fulfils orders from warehouse stock."""

    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse

    def fulfil(self, order: Order) -> None:
        for line in order.lines:
            available = self.warehouse.available(line.part_id)
            if available < line.quantity:
                raise InsufficientStockException(
                    f"need {line.quantity} of {line.part_id}, have {available}"
                )
            remaining = line.quantity
            for storage_bin in self.warehouse.bins:
                take = min(remaining, storage_bin.stored.get(line.part_id, 0))
                if take > 0:
                    storage_bin.take(line.part_id, take)
                    remaining -= take
                if remaining == 0:
                    break
        order.mark_shipped()