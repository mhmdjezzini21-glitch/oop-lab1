import pytest
from src.exceptions import QualityCheckFailedException
from src.models.quality import QualityStandard, QualityCheck

def test_invalid_standard():
    with pytest.raises(QualityCheckFailedException):
        QualityStandard("Q1", 1.5)

def test_quality_eval():
    std = QualityStandard("Q1", 0.05)
    check = QualityCheck("C1", std)
    assert check.pass_rate() == 0.0
    
    assert check.evaluate(100, 2) == True
    assert check.pass_rate() == 1.0
    
    assert check.evaluate(100, 10) == False
    assert check.pass_rate() == 0.5
    
    with pytest.raises(QualityCheckFailedException):
        check.evaluate(0, 0)
    with pytest.raises(QualityCheckFailedException):
        check.evaluate(10, 11)