# 生成器Generator
# 1.第三章學到的語法 => 生成器表達式
# (表達式 for 元素 in 可迭代對象 if 條件)
# 基本語法與列表list推導式類似，只是將方括號 [] 替換為圓括號 ()


def old_generator(n):
    return (x**3 for x in range(n))


# Python 告訴你這是一個生成器對象，而且指出這個生成器是通過生成器表達式（<genexpr>）在 old_generator 函數的局部範圍內創建的（<locals>）。
# <generator object old_generator.<locals>.<genexpr> at 0x0000013D9E8E6820>
print(old_generator(10))


# ===== 使用yield關鍵字定義Generaotr =====
def cube(n):
    for x in range(n):
        yield x**3


# 2. yield關鍵字定義生成器
# <generator object cube at 0x000001B394286890>
# 生成器函數：這種形式使用 yield 關鍵字來定義一個生成器函數。每次去跑這個generator object的時候，都會調用 yield，生成器會“產生”一個值，並在下一次迭代時從停止的位置繼續執行。
# 輸出：當你打印這個生成器時，Python 告訴你這是一個生成器對象，它是通過函數 cube 創建的。
print(cube(10))
for value in cube(10):
    print(value)

# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729


# ===== yield from =====
# yield from 是 Python 3 引入的一個語法，用於簡化生成器函數中委託（delegate）另一個生成器或可迭代對象的場景。
# 它可以幫助你從一個生成器中返回另一個生成器中的所有值，而不需要手動迭代或逐一 yield 這些值


def sub_generator():
    yield 1
    yield 2
    yield 3


def main_generator():
    yield from sub_generator()
    yield 4
    yield 5


for value in main_generator():
    print(value)

# 1
# 2
# 3
# 4
# 5


# yield from 還能夠捕捉子生成器的返回值（return）
# 子生成器返回值: 當 `sub_generator` 完成後，它會返回 `"Done"`，並且這個返回值被 `yield from` 捕捉到並賦值給 `result`。**
# 在主生成器中使用返回值: 接著，`main_generator` 可以使用這個返回值並將其 `yield` 出來。**
def sub_generator():
    # 子生成器：生成兩個值 1 和 2，然後返回 "Done"
    yield 1  # 第一次生成值 1
    yield 2  # 第二次生成值 2
    return "Done"  # 完成後返回 "Done"（這個返回值會被 yield from 捕獲）


def main_generator():
    # 主生成器：將 sub_generator 委託給 yield from，並捕獲返回值
    result = yield from sub_generator()  # 使用 yield from 來生成 sub_generator 的所有值
    yield result  # 將 sub_generator 的返回值 "Done" 生成出來
    yield 4  # 再生成值 4


# 迭代 main_generator，並打印每個生成的值
for value in main_generator():
    print(value)  # 順序打印 1, 2, "Done", 4

# 1
# 2
# Done
# 4
