def ask_for_a_int():
    while True:
        try:
            num = int(input("請輸入一個整數:"))
        except BaseException as err:
            print(err)
            print("錯誤數字，請重新輸入")
        else:
            return num


print(f"您輸入的數字是{ask_for_a_int()}")
