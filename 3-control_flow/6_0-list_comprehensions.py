# list列表推導式
# [表達式 for 元素 in 可迭代對象 if 條件]
# 生成平方數列表
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成偶數列表
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

