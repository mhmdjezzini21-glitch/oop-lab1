import pytest
from src.exceptions import MachineFailureException, MachineNotFoundException, CapacityExceededException
from src.models.production import Machine, ProductionLine, ProductionOrder

def test_machine_operations():
    m = Machine("M1", "CNC", 100)
    assert m.is_operational
    assert m.produce(10) == 10
    assert m.produced_units == 10
    m.break_down()
    assert not m.is_operational
    with pytest.raises(MachineFailureException):
        m.produce(5)
    m.repair()
    assert m.is_operational

def test_machine_invalid_capacity():
    with pytest.raises(MachineFailureException):
        Machine("M1", "CNC", 0)

def test_line_machines():
    line = ProductionLine("L1", "P1")
    m1 = Machine("M1", "CNC1", 100)
    m2 = Machine("M2", "CNC2", 80)
    line.add_machine(m1)
    line.add_machine(m2)
    assert line.bottleneck_capacity() == 80
    assert line.operational()
    m1.break_down()
    assert not line.operational()
    
    line.remove_machine("M2")
    assert line.bottleneck_capacity() == 100
    with pytest.raises(MachineNotFoundException):
        line.remove_machine("M3")

def test_empty_line():
    line = ProductionLine("L1", "P1")
    with pytest.raises(CapacityExceededException):
        line.bottleneck_capacity()

def test_production_order():
    order = ProductionOrder("O1", "P1", 100)
    assert not order.is_done()
    order.advance(50)
    assert order.completed_units == 50
    order.advance(60)
    assert order.completed_units == 100
    assert order.is_done()