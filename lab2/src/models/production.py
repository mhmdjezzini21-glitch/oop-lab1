"""Machines, production lines, and production orders."""

from src.exceptions import MachineFailureException, MachineNotFoundException, CapacityExceededException

class Machine:
    """A production machine."""

    def __init__(self, machine_id: str, name: str, capacity_per_hour: int):
        if capacity_per_hour <= 0:
            raise MachineFailureException("capacity must be positive")
        self.machine_id = machine_id
        self.name = name
        self.capacity_per_hour = capacity_per_hour
        self.is_operational = True
        self.produced_units = 0

    def break_down(self) -> None:
        self.is_operational = False

    def repair(self) -> None:
        self.is_operational = True

    def produce(self, units: int) -> int:
        if not self.is_operational:
            raise MachineFailureException(f"machine {self.machine_id} is down")
        self.produced_units += units
        return units

class ProductionLine:
    """A line composed of machines that produce a specific part."""

    def __init__(self, line_id: str, part_id: str):
        self.line_id = line_id
        self.part_id = part_id
        self.machines = []

    def add_machine(self, machine: Machine) -> None:
        self.machines.append(machine)

    def remove_machine(self, machine_id: str) -> None:
        for machine in self.machines:
            if machine.machine_id == machine_id:
                self.machines.remove(machine)
                return
        raise MachineNotFoundException(machine_id)

    def operational(self) -> bool:
        return bool(self.machines) and all(m.is_operational for m in self.machines)

    def bottleneck_capacity(self) -> int:
        if not self.machines:
            raise CapacityExceededException("line has no machines")
        return min(m.capacity_per_hour for m in self.machines)

class ProductionOrder:
    """An order to produce N units of a part on a line."""

    def __init__(self, order_id: str, part_id: str, quantity: int):
        if quantity <= 0:
            raise CapacityExceededException("quantity must be positive")
        self.order_id = order_id
        self.part_id = part_id
        self.quantity = quantity
        self.completed_units = 0

    def advance(self, units: int) -> int:
        self.completed_units = min(self.quantity, self.completed_units + units)
        return self.completed_units

    def is_done(self) -> bool:
        return self.completed_units >= self.quantity