"""Parts produced at the plant."""

from src.exceptions import InvalidPartDataException

MIN_PRICE = 0.01

class Part:
    """Base part with an id, name, and price."""

    def __init__(self, part_id: str, name: str, price: float, weight_kg: float):
        if not part_id or not name:
            raise InvalidPartDataException("id and name are required")
        if price < MIN_PRICE:
            raise InvalidPartDataException("price must be positive")
        if weight_kg < 0:
            raise InvalidPartDataException("weight must be non-negative")
        self.part_id = part_id
        self.name = name
        self.price = price
        self.weight_kg = weight_kg

    def category(self) -> str:
        return "part"

    def __repr__(self) -> str:
        return f"{self.category()}({self.part_id}, {self.name})"

class EnginePart(Part):
    """Engine component."""

    def __init__(self, part_id, name, price, weight_kg, horsepower: int):
        super().__init__(part_id, name, price, weight_kg)
        self.horsepower = horsepower

    def category(self) -> str:
        return "engine"

class BrakePart(Part):
    """Braking system component."""

    def __init__(self, part_id, name, price, weight_kg, is_abs: bool):
        super().__init__(part_id, name, price, weight_kg)
        self.is_abs = is_abs

    def category(self) -> str:
        return "brake"

class SuspensionPart(Part):
    """Suspension component."""

    def __init__(self, part_id, name, price, weight_kg, stiffness: float):
        super().__init__(part_id, name, price, weight_kg)
        self.stiffness = stiffness

    def category(self) -> str:
        return "suspension"

class ElectricalPart(Part):
    """Electrical component."""

    def __init__(self, part_id, name, price, weight_kg, voltage: float):
        super().__init__(part_id, name, price, weight_kg)
        self.voltage = voltage

    def category(self) -> str:
        return "electrical"