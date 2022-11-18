from account import account

def test_init():
    acc1 = account("Uma")
    assert acc1.getname() == "Uma"
    assert acc1.getbalance() == 0

def test_deposit():
    acc1 = account("Uma")
    acc1.deposit(20)
    assert acc1.getbalance() == 20


def test_withdraw():
    acc1 = account("Uma")
    acc1.deposit(100)
    acc1.withdraw(20)
    assert acc1.getbalance() == 80
