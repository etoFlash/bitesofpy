import pytest

from account import Account


def test_account():
    acc_alex = Account("Alex", amount=5)
    acc_mike = Account("Mike", amount=55)
    assert acc_alex.balance == 5
    assert acc_alex != acc_mike
    assert not acc_alex == acc_mike
    assert acc_alex < acc_mike
    acc_alex.add_transaction(50)
    assert acc_alex[0] == 50
    assert acc_alex == acc_mike
    acc_alex.add_transaction(60)
    assert acc_alex[1] == 60
    assert acc_alex > acc_mike
    assert len(acc_alex) == 2
    assert acc_alex.balance == 115
    assert str(acc_alex) == "Account of Alex with starting amount: 5"
    assert repr(acc_alex) == "Account('Alex', 5)"
    acc_alex += acc_mike
    assert str(acc_alex) == "Account of Alex&Mike with starting amount: 60"
    assert acc_alex.balance == 170
    with pytest.raises(ValueError):
        acc_mike.add_transaction(None)
