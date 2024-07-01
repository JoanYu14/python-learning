# @property 的基本用法
# 有時，當我們存取或指派物件的屬性時，我們不想直接存取或指派它。
# @property 裝飾器是 Python 中的內建裝飾器，有助於輕鬆定義虛擬屬性。

# 將方法轉換為屬性:
# 使用 `@property` 可以將一個方法轉換為一個屬性，這樣在訪問該方法時不需要使用括號。
# 1. 定義getter方法:
# 使用 `@property` 定義一個方法，該方法會作為屬性的getter方法。
# 2. 定義setter方法:
# 使用 `@屬性名稱.setter` 定義一個方法，該方法會作為屬性的setter方法。
# 3. 定義deleter方法:
# 使用 `@屬性名稱.deleter` 定義一個方法，該方法會作為屬性的deleter方法。

class Employee():
    def __init__(self):
        self.income = 0

    def make_money(self,money):
        self.income += money
    
    # 定義getter
    @property
    def tax_amount(self):
        return self.income * 0.05
    
    # 設定tax_amount的金額
    @tax_amount.setter
    def tax_amount(self,tax_number):
        # 當objectname.amount = tax_number時會觸發income會=tax_number * 20
        # 並且tax_mount的值被更改為tax_number
        self.income = tax_number * 20
    

        
    
joan = Employee()
joan.make_money(100) 
print(f"joan當前的收入為:{joan.income}") # joan當前的收入為:100
print(f"joan當前要繳的稅為:{joan.tax_amount}") # joan當前要繳的稅為:5.0
joan.tax_amount = 200
print(f"joan當前要繳的稅為:{joan.tax_amount}") # joan當前要繳的稅為:200.0
print(f"joan當前的收入為:{joan.income}") # joan當前的收入為:4000

