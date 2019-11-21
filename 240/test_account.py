import pytest

from account import Account


def test_account():
    acc_alex = Account("Alex", amount=5)
    acc_mike = Account("Mike", amount=55)
    acc_sid = Account("Sid")
    assert acc_sid.balance == 0
    assert len(acc_sid) == 0
    acc_sid = acc_alex + acc_mike
    assert acc_alex.balance == 5
    assert acc_alex != acc_mike
    assert not acc_alex == acc_mike
    assert acc_alex < acc_mike
    assert acc_alex <= acc_mike
    acc_alex.add_transaction(50)
    assert acc_alex[0] == 50
    assert acc_alex == acc_mike
    acc_alex.add_transaction(60)
    assert acc_alex[1] == 60
    assert acc_alex > acc_mike
    assert not acc_alex.balance < acc_mike.balance
    assert acc_alex >= acc_mike
    assert len(acc_alex) == 2
    assert acc_alex.balance == 115
    assert acc_alex.balance >= 115
    assert acc_alex.balance <= 115
    assert str(acc_alex) == "Account of Alex with starting amount: 5"
    assert repr(acc_alex) == "Account('Alex', 5)"
    acc_alex += acc_mike
    assert str(acc_alex) == "Account of Alex&Mike with starting amount: 60"
    print("test123", repr(acc_alex))
    assert acc_alex.balance == 170
    acc_alex.add_transaction(-171)
    assert acc_alex < acc_mike and not acc_alex == acc_mike
    acc_alex2 = Account("Alex2", amount=acc_alex.balance + 10000000000000000000)
    assert not acc_alex2 < acc_alex2
    assert acc_alex.balance <= 10000000000000000000
    with pytest.raises(ValueError) as excinfo:
        acc_mike.add_transaction(None)
    assert str(excinfo.value) == "please use int for amount"
    with pytest.raises(ValueError) as excinfo:
        acc_mike.add_transaction("")
    assert str(excinfo.value) == "please use int for amount"
    with pytest.raises(TypeError):
        acc_test = Account("Test", "wrong")
        acc_test.add_transaction(1)
        print(acc_test.balance)
    with pytest.raises(AttributeError):
        acc_alex += 123
