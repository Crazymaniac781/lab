class Account:
    """
    account class is to create  objects for an account with some basic methods deposit , withdraw , getbalance and getname
    """
    def __init__(self, name: str):
        """
        Constructor to initialise the objects of account class
        :param name: The Person's name
        """
        self.__account_name = name
        self.__account_balance = 0
    def deposit(self, amount: int) -> bool:
        """
        deposit(amount) method deposits or add specified amount to the account balance
        :param amount: How much the person is depositing
        :return: Checking to see if they are adding more than 0 then return True or False
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: int) -> bool:
        """
        withdraw(amount) method to withdraw the specified amount from the account balance
        :param amount: How much they are withdrawing
        :return: Checking to see if they have enough money to withdraw said amount and if the amount is more than 0
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - amount
                return True
            else:
                return False
        else:
            return False
    def getbalance(self) -> int:
        """
        getter method to get the private variable __account_balance alias bank balance amount
        :return: Account balance
        """
        return self.__account_balance
    def getname(self) -> str:
        """
        getter method to get the private variable __account_name alias bank holder name
        :return: Name associated with the account
        """
        return self.__account_name