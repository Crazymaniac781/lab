from account import *
class Test:

    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def test_init(self):
        assert self.a1.getname() == 'John'
        assert self.a1.getbalance() == 0
        assert self.a2.getname() == 'Jane'
        assert self.a2.getbalance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.getbalance() == 0
        self.a1.deposit(0)
        assert self.a1.getbalance() == 0
        self.a1.deposit(1)
        assert self.a1.getbalance() == 1

    def test_withdraw(self):
        assert self.a2.withdraw(-2) is False
        assert self.a2.withdraw(2) is False
        assert self.a2.withdraw(0) is False
        self.a2.deposit(5)
        assert self.a2.withdraw(2) == True

    def tear_down(self):
        del self.a1
        del self.a2