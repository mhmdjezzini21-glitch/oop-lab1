import pytest
from src.exceptions import InvalidPartDataException
from src.models.parts import BrakePart, ElectricalPart, EnginePart, Part, SuspensionPart

def test_part_valid():
    p = Part("P1", "x", 1.0, 0.5)
    assert p.category() == "part"

def test_part_negative_price():
    with pytest.raises(InvalidPartDataException):
        Part("P1", "x", -1, 0.5)

def test_part_negative_weight():
    with pytest.raises(InvalidPartDataException):
        Part("P1", "x", 1, -0.5)

def test_engine_category():
    assert EnginePart("P", "x", 1, 1, 100).category() == "engine"

def test_brake_category():
    assert BrakePart("P", "x", 1, 1, True).category() == "brake"

def test_suspension_category():
    assert SuspensionPart("P", "x", 1, 1, 1.0).category() == "suspension"

def test_electrical_category():
    assert ElectricalPart("P", "x", 1, 1, 12.0).category() == "electrical"

def test_part_repr():
    assert "part(P1, x)" in repr(Part("P1", "x", 1, 1))