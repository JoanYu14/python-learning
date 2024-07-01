# 集合推導式
# {表達式 for 元素 in 可迭代對象 if 條件}
# 生成平方數集合
squares_set = {x**2 for x in range(10)}
print(squares_set)  # {0, 1, 4, 36, 9, 16, 49, 64, 81, 25}

# 生成唯一字母集合
letters = {char for char in "hello world"}
print(letters)  # {'h', 'd', 'e', 'l', 'o', 'r', 'w'}