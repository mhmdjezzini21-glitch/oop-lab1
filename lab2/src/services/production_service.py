from src.exceptions import MachineFailureException
from src.models.production import ProductionOrder, ProductionLine

class ProductionService:
    """Runs production orders against lines."""

    def run_order(self, production_order: ProductionOrder, line: ProductionLine) -> int:
        if not line.operational():
            raise MachineFailureException("line is not operational")
        capacity = line.bottleneck_capacity()
        produced = production_order.advance(capacity)
        for machine in line.machines:
            machine.produce(capacity)
        return produced