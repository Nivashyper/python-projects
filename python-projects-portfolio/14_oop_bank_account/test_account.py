from account import BankAccount
import pytest

def test_flow():
    a = BankAccount("Nivas", 100)
    a.deposit(50)
    assert a.balance == 150
    a.withdraw(25)
    assert a.balance == 125
    with pytest.raises(ValueError):
        a.withdraw(1000)
