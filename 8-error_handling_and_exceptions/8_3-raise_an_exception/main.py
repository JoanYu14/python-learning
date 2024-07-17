# 假設模組名為 something，並且已經包含 NegativeNumberException 類和 enter_age 函數
import something

# 使用無限循環讓用戶重複輸入直到輸入合法的年齡
while True:
    try:
        # 從用戶那裡獲取輸入的年齡，並將其轉換為整數
        age = int(input("請輸入年齡:"))

        # 呼叫 something 模組中的 enter_age 函數
        something.enter_age(age)
    except something.NegativeNumberException as error:
        # 捕捉 NegativeNumberException 並打印錯誤訊息
        print(error)
    except Exception as error:
        # 捕捉所有其他的例外並打印錯誤訊息
        print(error)
    else:
        # 如果沒有例外發生，則跳出循環
        break


# 請輸入年齡:-1
# 錯誤:年齡不能小於0

# 請輸入年齡:p
# invalid literal for int() with base 10: 'p'
# 請輸入年齡:3
# 你的年齡是奇數
