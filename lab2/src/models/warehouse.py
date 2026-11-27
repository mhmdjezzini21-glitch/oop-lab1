"""Warehouse and stock."""

from src.exceptions import InsufficientStockException, CapacityExceededException

class StorageBin:
    """A storage location with limited capacity."""

    def __init__(self, bin_id: str, capacity_units: int):
        if capacity_units <= 0:
            raise CapacityExceededException("capacity must be positive")
        self.bin_id = bin_id
        self.capacity_units = capacity_units
        self.stored = {}

    def store(self, part_id: str, quantity: int) -> None:
        current = self.stored.get(part_id, 0)
        if current + quantity > self.capacity_units:
            raise CapacityExceededException(f"bin {self.bin_id} is full")
        self.stored[part_id] = current + quantity

    def take(self, part_id: str, quantity: int) -> int:
        current = self.stored.get(part_id, 0)
        if current < quantity:
            raise InsufficientStockException(f"not enough {part_id} in {self.bin_id}")
        self.stored[part_id] = current - quantity
        return quantity

class Warehouse:
    """A warehouse composed of storage bins."""

    def __init__(self, warehouse_id: str, address: str):
        self.warehouse_id = warehouse_id
        self.address = address
        self.bins = []

    def add_bin(self, storage_bin: StorageBin) -> None:
        self.bins.append(storage_bin)

    def total_units(self) -> int:
        return sum(sum(b.stored.values()) for b in self.bins)

    def find_bin_with(self, part_id: str) -> StorageBin:
        for storage_bin in self.bins:
            if storage_bin.stored.get(part_id, 0) > 0:
                return storage_bin
        raise InsufficientStockException(f"part {part_id} not in stock")

    def available(self, part_id: str) -> int:
        return sum(b.stored.get(part_id, 0) for b in self.bins)