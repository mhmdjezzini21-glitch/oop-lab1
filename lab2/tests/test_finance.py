import pytest
from src.exceptions import InsufficientFundsException, SupplierNotFoundException
from src.models.finance import Account, Transaction, Supplier, Invoice, SupplierRegistry

def test_account_ops():
    a = Account("A1", 100.0)
    a.deposit(50.0)
    assert a.balance == 150.0
    a.withdraw(30.0)
    assert a.balance == 120.0
    
    with pytest.raises(InsufficientFundsException):
        a.deposit(-10)
    with pytest.raises(InsufficientFundsException):
        a.withdraw(200)

def test_transaction():
    a1 = Account("A1", 100.0)
    a2 = Account("A2", 50.0)
    t = Transaction("T1", a1, a2, 30.0)
    t.execute()
    assert a1.balance == 70.0
    assert a2.balance == 80.0
    assert t.executed

def test_supplier():
    s = Supplier("S1", "Steel", "iron")
    s.record_delivery(10)
    assert s.deliveries == 10
    with pytest.raises(ValueError):
        s.record_delivery(-5)

def test_invoice():
    i = Invoice("I1", 500.0)
    assert not i.paid
    i.pay()
    assert i.paid

def test_supplier_registry():
    r = SupplierRegistry()
    s = Supplier("S1", "Steel", "iron")
    r.register(s)
    assert r.get("S1") == s
    with pytest.raises(SupplierNotFoundException):
        r.get("S2")