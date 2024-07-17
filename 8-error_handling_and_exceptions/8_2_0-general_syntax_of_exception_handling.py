def division(x, y):
    try:
        result = int(x) / int(y)
    except ZeroDivisionError as error:
        print(error)
        print("y不能為0")
    except BaseException as basic_error:
        print(basic_error)
        print("其他錯誤")
    else:
        print("division函數執行成功")
        return result
    finally:
        print("函數結束")


input_string = input("請輸入x與y，以空白分隔")
x, y = input_string.split(" ")
print(division(x, y))

# 請輸入x與y，以空白分隔1 2
# division函數執行成功
# 函數結束
# 0.5

# 請輸入x與y，以空白分隔1 0
# division by zero
# y不能為0
# 函數結束
# None

# 請輸入x與y，以空白分隔1 sta
# invalid literal for int() with base 10: 'sta'
# 其他錯誤
# 函數結束
# None
