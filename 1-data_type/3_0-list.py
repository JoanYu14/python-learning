# 列表方法示例

# len()
lst = [1, 2, 3, 4, 5]
print("len(lst):", len(lst))  # 5

# 索引
print("lst[0]:", lst[0])  # 1
print("lst[-1]:", lst[-1])  # 5

# count()
lst = [1, 2, 3, 4, 1, 2, 1]
print("lst.count(1):", lst.count(1))  # 3

# index()
lst = [1, 2, 3, 4, 5]
print("lst.index(3):", lst.index(3))  # 2

# set()
lst = [1, 2, 3, 4, 1, 2, 1]
print("set(lst):", set(lst))  # {1, 2, 3, 4}

# 列表拼接
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print("lst1 + lst2:", lst1 + lst2)  # [1, 2, 3, 4, 5, 6]

# 列表乘法
lst = [1, 2, 3]
print("lst * 3:", lst * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 列表是可變的
lst = [1, 2, 3]
lst[0] = 10
print("lst:", lst)  # [10, 2, 3]

lst.append(4)
print("lst:", lst)  # [10, 2, 3, 4]

del lst[1]
print("lst:", lst)  # [10, 3, 4]
