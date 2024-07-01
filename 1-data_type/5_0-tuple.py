# 元組方法示例

# len()
tup = (1, 2, 3, 4, 5)
print(f"tup={tup}")
print("len(tup):", len(tup))  # 5

# 索引
print("tup[0]:", tup[0])  # 1
print("tup[-1]:", tup[-1])  # 5
print(f"tup[2::]=>{tup[2::]}")

# count()
tup = (1, 2, 3, 2, 4, 2)
print("tup.count(2):", tup.count(2))  # 3

# index()
tup = (1, 2, 3, 4, 5)
print("tup.index(3):", tup.index(3))  # 2

# set()
tup = (1, 2, 3, 2, 4, 1)
print("set(tup):", set(tup))  # {1, 2, 3, 4}

# tuple內的可變動元素
tup = ([1,2,3],"Joan")
#tup[0] = [1,2] => 拋出錯誤TypeError: 'tuple' object does not support item assignment
tup[0][1] = "4" # 可以正常執行
print(tup) # ([1, '4', 3], 'Joan')
# 但這種tuple不能當作dictionary的key，如果要當作key的話，tuple內的所有元素都要是不可變的資料型別

# 15 => Yes
# "Bob" => Yes
# ("Tom", [14,23,27]) => No
# ["filename", (15,14)] => No
# "filename" => Yes
# ("filename", 25, "extension") => Yes