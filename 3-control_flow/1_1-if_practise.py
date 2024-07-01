#JavaScript 與 Python 在處理函數定義和調用的順序上有一些不同。
# 在 JavaScript 中，由於函數提升（hoisting）的特性，函數可以在定義之前被調用。然而，在 Python 中沒有這種特性，所以函數必須在調用之前定義。
def hungryOrNot(ans):
    if(ans=="Y"):
        return True
    elif(ans=="N"):
        return False
    else:
        return "輸入錯誤"

# input預設型別為String
name = input("請輸入您的名字：")
hungry = hungryOrNot(input("你現在餓嗎?(Y/N)"))
cash = int(input("你現在身上有多少錢:"))

if (str(hungry)!="True" and str(hungry)!="False"):
    print("輸入錯誤")
elif (hungry) and (cash>=30):
    print(f"{name}餓了所以買了一份早餐")
elif (hungry) and (cash<30):
    print(f"{name}餓了但錢不夠買早餐")
elif (not hungry) and (cash>=30):
    print(f"{name}雖然錢夠，但並不餓")
else:
    print(f"{name}雖然錢不夠但並不餓")

