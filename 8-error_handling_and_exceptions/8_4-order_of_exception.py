#  LookupError 類別有 2 個子類別:1.LookupError 2.IndexError
# 這意味著 IndexError 和 KeyError 的任何實例也屬於 LookupError 類別。
# 如果我們將 LookupError 放在 IndexError 或 KeyError 之前，那麼 LookupError 將捕獲所有這兩種類型的錯誤，並且永遠不會到達 IndexError 和 KeyError 程式碼。
try:
    lst = [1, 2, 3]
    print(lst[3])

# 若將以下兩個except的順序互換的話IndexError的程式碼會變成半透明的，代表永遠不會被執行到
except IndexError as error:
    dic = {"1": 1}
    # print(f"indexError:{error}")
    # print(dic["2"])
    # During handling of the above exception, another exception occurred:
    # KeyError: '2'


except LookupError as error:
    print(f"LookupError:{error}")
