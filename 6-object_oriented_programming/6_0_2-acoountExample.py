class Account():
    all_account = []

    def __init__(self,account_number,owner_name,balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.__class__.all_account.append(account_number)

    def deposit(self,money):
        self.balance += money
        return f"{self.owner_name}存入{money}元，帳戶餘額為:{self.balance}"
    
    def withdraw(self,money):
        self.balance -= money
        return f"{self.owner_name}提出{money}元，帳戶餘額為:{self.balance}"

    def get_account_info(self):
        return f"帳號:{self.account_number}，所有者姓名:{self.owner_name}，餘額:{self.balance}"
    
    def transfer(self,money,user):
        self.balance-=money
        user.balance+=money
    
    @classmethod
    def get_account_count(cls):
        return f"目前總共有{len(cls.all_account)}個帳戶"


user1 = Account(1,"Kevin")
user2 = Account(2,"Joan",300)
print(Account.get_account_count())
print(f"{user1.owner_name}的餘額目前為:{user1.balance}\n{user1.deposit(100)}\n現在{user1.owner_name}餘額有{user1.balance}元")
print(f"{user2.owner_name}的餘額目前為:{user2.balance}\n{user2.withdraw(100)}\n現在{user2.owner_name}餘額有{user2.balance}元")
user1.transfer(100,user2)
print(f"{user1.owner_name}的餘額目前為:{user1.balance}\n\n現在{user1.owner_name}餘額有{user1.balance}元")
print(f"{user2.owner_name}的餘額為{user2.balance}")
# print(user1.deposit(100))
# print(user1.balance)