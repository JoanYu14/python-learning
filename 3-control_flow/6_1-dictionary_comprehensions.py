# 字典推導式
# {鍵表達式: 值表達式 for 元素 in 可迭代對象 if 條件}
# 將數字及其平方生成字典
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 將字符串長度生成字典
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words}
print(lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}

names = ["Joan","Jessica","Kevin","Mars"]
ages = [23,28,30]
dir = dict(zip(names,ages))
print(dir)
newDir = {("Teacher:" + name) if age + 2 >= 30 else ("Student:" + name): age + 2 for name, age in zip(names, ages)}
print(newDir)

