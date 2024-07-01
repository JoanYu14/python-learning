# 編寫一個程式，接受使用者的輸入並讓他們猜測秘密數字是什麼。
# 秘密數字範圍為1至100；每次用戶給予猜測時，程式都應該更新範圍。
secret = int(input("請輸入秘密數字:"))
min = 1
max = 100
while True:
    num = int(input(f"請輸入猜測的數字(範圍:{min}~{max}):"))
    if num>max or num<min:
        print("輸入數字不在範圍內")  
        continue # 直接下一圈較不耗資源  
    elif num>secret:
        max=num
        continue
    elif num<secret:
        min=num
        continue
    else:
        print(f"正確!秘密數字為{num}")
        break
    