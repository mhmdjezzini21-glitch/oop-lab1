"""Quality control."""

from src.exceptions import QualityCheckFailedException

class QualityStandard:
    """A standard a batch is checked against."""

    def __init__(self, standard_id: str, max_defect_ratio: float):
        if not 0 <= max_defect_ratio <= 1:
            raise QualityCheckFailedException("ratio must be in 0..1")
        self.standard_id = standard_id
        self.max_defect_ratio = max_defect_ratio

class QualityCheck:
    """Checks a batch against a standard."""

    def __init__(self, check_id: str, standard: QualityStandard):
        self.check_id = check_id
        self.standard = standard
        self.checked_batches = 0
        self.failed_batches = 0

    def evaluate(self, batch_size: int, defects: int) -> bool:
        if batch_size <= 0:
            raise QualityCheckFailedException("batch size must be positive")
        if defects < 0 or defects > batch_size:
            raise QualityCheckFailedException("invalid defect count")
        ratio = defects / batch_size
        self.checked_batches += 1
        if ratio > self.standard.max_defect_ratio:
            self.failed_batches += 1
            return False
        return True

    def pass_rate(self) -> float:
        if self.checked_batches == 0:
            return 0.0
        passed = self.checked_batches - self.failed_batches
        return round(passed / self.checked_batches, 4)