# Guard Clauses and Exception Handling(保護子句與異常處理)


def division(a, b):
    if (type(a) == int) and (type(b) == int):
        if b != 0:
            return a / b
        else:
            return "第二個參數不能為0"
    else:
        return "參數只能是整數"


def exceptionDivision(a, b):
    if (type(a) != int) or (type(b) != int):
        raise TypeError("參數只能是整數")
    if b == 0:
        raise ZeroDivisionError("第二個參數不能為0")
    else:
        return a / b


print(division(5, 2))  # 2.5K
print(division(5, 0))  # 第二個參數不能為0
print(division("a", 2))  # 參數只能是整數

print("===")

try:
    print(exceptionDivision(5, 2))  # 2.5
    print(exceptionDivision(5, 0))  # 第二個參數不能為0
except Exception as error:
    print(error)
    print(type(error))  # <class 'ZeroDivisionError'>
