# 基本示例
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped) # <zip object at 0x0000025183EFA400>
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 處理長度不一致的可迭代對象
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 解壓（unzip）
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*zipped)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# 與 for 迴圈結合使用
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# 輸出:
# Alice scored 85
# Bob scored 90
# Charlie scored 95
#創建字典
keys = ['name', 'age', 'gender']
values = ['Alice', 25, 'Female']
dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Alice', 'age': 25, 'gender': 'Female'}

