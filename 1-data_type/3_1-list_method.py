# 列表方法示例

# insert(index,element)
lst = [1, 2, 3]
lst.insert(1, 4)
lst.insert(6,8)
print("insert:", lst)  # [1, 4, 2, 3]

# remove(index)
lst = [1, 2, 3, 2, 4]
lst.remove(2)
print("remove:", lst)  # [1, 3, 2, 4]

# clear()
lst = [1, 2, 3]
lst.clear()
print("clear:", lst)  # []

# sort()
lst = [3, 1, 4, 2]
lst.sort()
print("sort (ascending):", lst)  # [1, 2, 3, 4]

lst.sort(reverse=True)
print("sort (descending):", lst)  # [4, 3, 2, 1]

# reverse()
lst = [1, 2, 3]
lst.reverse()
print("reverse:", lst)  # [3, 2, 1]

# append()
lst = [1, 2, 3]
lst.append(4)
print("append:", lst)  # [1, 2, 3, 4]

# pop()
lst = [1, 2, 3]
print("pop (last):", lst.pop())  # 3
print("list after pop:", lst)  # [1, 2]


lst = [1, 2, 3]
print("pop (index 1):", lst.pop(1))  # 2
print("list after pop:", lst)  # [1, 3]

# copy()
print("")
lst = [1, 2, 3]
lst2=lst
# copy by reference，也就是lst2與lst其實是指向同一個記憶體位置
lst_copy = lst.copy()
print("copy:", lst_copy)  # [1, 2, 3]
print(f"before lst.append(4) lst=>{lst}，lst2=>{lst2}") # before lst.append(4) lst=>[1, 2, 3]，lst2=>[1, 2, 3]

lst.append(4)
print(f"after lst.append(4) lst=>{lst}，lst2=>{lst2}")  # after lst.append(4) lst=>[1, 2, 3, 4]，lst2=>[1, 2, 3, 4]
print(f"lst2{lst2}")
print("copied list:", lst_copy)  # [1, 2, 3] not change

lst = [0,0,7]
print(f'0出現的次數{lst.count(0)}')
print(f'7出現的次數{lst.count(7)}')
