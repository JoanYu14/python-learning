# LBYL(Look Before You Leap)
# 先做驗證(if y == 0)確認沒問題才做下一步
def division1(x, y):
    if y == 0:
        print("不能除0")
        return None
    else:
        return x / y


# EAFP (Easier to Ask Forgiveness than Permission)
# 不管怎樣，先做了再說，錯了的話再處裡
def division2(x, y):
    try:
        return x / y

    # 如果在執行 x / y 時發生了 ZeroDivisionError，也就是當 y 等於 0 時，程式會立即中斷正在執行的運算，並進入 except 區塊。
    except ZeroDivisionError:
        print("不能除0")
        return None


# # LBYL寫訪
# def save_a_file_LBYL():
#     result = save.prefs()
#     if result == "error":
#         print("Preference not save")
#         return
#     result = save_test()
#     if result == "error":
#         print("Not enough memory")
#         return
#     result = save_formmat()
#     if result == "error":
#         print("Format not saved")
#         return

# # EAFP寫法
# def save_a_file_EAFP():
#     try:
#         result = save_prefs()
#         result = save_test()
#         result = save_formmat()
#     except:
#         print("Something went wrong...")
