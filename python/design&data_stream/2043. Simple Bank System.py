
class Bank:
    '''
    input:nested list items,
    account number:1-n,so index should be -1,etc: account1 position in the list should be list[0]
    may need a helpful function to check if the account within this boundry:1-n
    '''

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
    def isvalid(self,account)->bool:
        if 1 <= account <= self.n:
            return True
        else:
            return False


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isvalid(account1) or not self.isvalid(account2):
            return False
        index1 = account1 - 1
        index2 = account2 - 1
        if self.balance[index1] < money:
            return False
        self.balance[index1] -= money
        self.balance[index2] += money
        return True


    def deposit(self, account: int, money: int) -> bool:
        if not self.isvalid(account):
            return False
        index = account - 1
        self.balance[index] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isvalid(account):
            return False
        index = account - 1
        if self.balance[index] < money:
            return False
        self.balance[index] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)