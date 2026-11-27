import pytest
from src.exceptions import InvalidEmployeeDataException, InvalidShiftException
from src.models.people import Employee, Engineer, Manager, Shift, Worker

def test_employee_computes_base_salary():
    e = Employee("E1", "A", 10.0)
    e.log_hours(160)
    assert e.compute_salary() == 1600.0

def test_employee_computes_overtime():
    e = Employee("E1", "A", 10.0)
    e.log_hours(170)
    assert e.compute_salary() == pytest.approx(1600 + 10 * 15)

def test_employee_rejects_negative_hours():
    e = Employee("E1", "A", 10.0)
    with pytest.raises(InvalidShiftException):
        e.log_hours(-1)

def test_invalid_employee_data():
    with pytest.raises(InvalidEmployeeDataException):
        Employee("", "A")

def test_worker_counts_tasks():
    w = Worker("W1", "B", "L1")
    w.complete_task()
    assert w.tasks_completed == 1

def test_engineer_adds_design():
    e = Engineer("E1", "C", "eng")
    e.add_design("P1")
    assert "P1" in e.designs

def test_manager_team():
    m = Manager("M1", "D", "prod")
    m.add_to_team(Employee("E1", "A"))
    assert m.team_size() == 1

def test_shift_duration():
    s = Shift("S1", 8, 16)
    assert s.duration() == 8

def test_shift_invalid_hours():
    with pytest.raises(InvalidShiftException):
        Shift("S1", 16, 8)

def test_shift_assign():
    s = Shift("S1", 8, 16)
    s.assign(Worker("W1", "A", "L1"))
    assert len(s.assigned_workers) == 1