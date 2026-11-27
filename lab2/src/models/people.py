"""People working at the plant."""

from src.exceptions import InvalidEmployeeDataException, InvalidShiftException

HOURLY_RATE = 15.0
OVERTIME_MULTIPLIER = 1.5
STANDARD_HOURS = 160

class Employee:
    """Base employee with a name and an id."""

    def __init__(self, employee_id: str, full_name: str, hourly_rate: float = HOURLY_RATE):
        if not employee_id or not full_name:
            raise InvalidEmployeeDataException("id and name are required")
        if hourly_rate <= 0:
            raise InvalidEmployeeDataException("hourly rate must be positive")
        self.employee_id = employee_id
        self.full_name = full_name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def log_hours(self, hours: int) -> None:
        if hours < 0:
            raise InvalidShiftException("hours cannot be negative")
        self.hours_worked += hours

    def compute_salary(self) -> float:
        base = min(self.hours_worked, STANDARD_HOURS) * self.hourly_rate
        overtime = max(0, self.hours_worked - STANDARD_HOURS) * self.hourly_rate * OVERTIME_MULTIPLIER
        return round(base + overtime, 2)

    def __repr__(self) -> str:
        return f"Employee({self.employee_id}, {self.full_name})"

class Worker(Employee):
    """Shop-floor worker attached to a machine line."""

    def __init__(self, employee_id, full_name, line_code: str, hourly_rate=HOURLY_RATE):
        super().__init__(employee_id, full_name, hourly_rate)
        self.line_code = line_code
        self.tasks_completed = 0

    def complete_task(self) -> None:
        self.tasks_completed += 1

class Engineer(Employee):
    """Engineer who designs parts."""

    def __init__(self, employee_id, full_name, specialization: str, hourly_rate=HOURLY_RATE):
        super().__init__(employee_id, full_name, hourly_rate)
        self.specialization = specialization
        self.designs = []

    def add_design(self, part_id: str) -> None:
        self.designs.append(part_id)

class Manager(Employee):
    """Manager with a team of employees."""

    def __init__(self, employee_id, full_name, department: str, hourly_rate=HOURLY_RATE):
        super().__init__(employee_id, full_name, hourly_rate)
        self.department = department
        self.team = []

    def add_to_team(self, employee: Employee) -> None:
        self.team.append(employee)

    def team_size(self) -> int:
        return len(self.team)

class Shift:
    """A work shift with a start and end hour."""

    def __init__(self, shift_id: str, start_hour: int, end_hour: int):
        if not 0 <= start_hour < 24 or not 0 <= end_hour <= 24:
            raise InvalidShiftException("hours must be within 0..24")
        if start_hour >= end_hour:
            raise InvalidShiftException("shift start must precede end")
        self.shift_id = shift_id
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.assigned_workers = []

    def duration(self) -> int:
        return self.end_hour - self.start_hour

    def assign(self, worker: Worker) -> None:
        self.assigned_workers.append(worker)