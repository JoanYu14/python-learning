# 定義一個自訂的例外類別，繼承自 BaseException
class NegativeNumberException(BaseException):
    # 初始化方法，接收年齡參數
    def __init__(self, age):
        # 呼叫父類別的初始化方法
        super().__init__()
        # 將年齡參數賦值給實例變數
        self.age = age
        # 如果年齡小於0，則打印錯誤訊息
        if age < 0:
            print("錯誤:年齡不能小於0")


# 定義一個函數，用於輸入年齡並檢查其有效性
def enter_age(age):
    # 如果年齡小於0，則引發 NegativeNumberException
    if age < 0:
        raise NegativeNumberException(age)

    # 如果年齡是偶數，打印相應訊息
    if age % 2 == 0:
        print("你的年齡是偶數")
    # 否則，打印年齡是奇數的訊息
    else:
        print("你的年齡是奇數")
