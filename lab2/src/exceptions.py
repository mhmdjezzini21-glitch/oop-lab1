"""Custom exception hierarchy for the automotive parts plant domain."""

class PlantException(Exception):
    """Base exception for all plant-related errors."""

class InvalidPartDataException(PlantException):
    """Raised when a part has invalid attributes."""

class PartNotFoundException(PlantException):
    """Raised when a part cannot be located in the catalog."""

class InsufficientStockException(PlantException):
    """Raised when stock is too low to fulfil a request."""

class MachineFailureException(PlantException):
    """Raised when a machine is broken or offline."""

class MachineNotFoundException(PlantException):
    """Raised when a machine id does not exist."""

class InvalidOrderDataException(PlantException):
    """Raised when an order has invalid data."""

class OrderNotFoundException(PlantException):
    """Raised when an order id does not exist."""

class InvalidEmployeeDataException(PlantException):
    """Raised when employee data is invalid."""

class EmployeeNotFoundException(PlantException):
    """Raised when an employee id does not exist."""

class InsufficientFundsException(PlantException):
    """Raised when an account lacks funds for a transaction."""

class QualityCheckFailedException(PlantException):
    """Raised when a quality check rejects a batch."""

class SupplierNotFoundException(PlantException):
    """Raised when a supplier cannot be found."""

class InvalidShiftException(PlantException):
    """Raised when a shift assignment is invalid."""

class CapacityExceededException(PlantException):
    """Raised when warehouse capacity is exceeded."""