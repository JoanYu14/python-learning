# Set基本用法介紹
mySet = set() # 若是直接用空的大括號{}會變成dictionary
notSet = {}
# mySet的type為<class 'set'>，notSet的type為<class 'dict'>
print(f"mySet的type為{type(mySet)}，notSet的type為{type(notSet)}")

myNewSet = set({1,2,3,3,3})
print(myNewSet) # {1, 2, 3}

# Set方法示例
# add()
s = {1, 2, 3}
s.add(4)
print("add(4):", s)  # {1, 2, 3, 4}

s.add(2)
print("add(2):", s)  # {1, 2, 3, 4}

# clear()
s = {1, 2, 3}
s.clear()
print("clear():", s)  # set()

# copy()
s = {1, 2, 3}
s_copy = s.copy()
print("copy():", s_copy)  # {1, 2, 3}

s.add(4)
print("original set after add(4):", s)  # {1, 2, 3, 4}
print("copied set:", s_copy)  # {1, 2, 3}

# discard()
# 說明：從集合中移除一個元素。如果元素不存在於集合中，不會拋出錯誤。
s = {1, 2, 3}
s.discard(2)
print("discard(2):", s)  # {1, 3}

s.discard(4)
print("discard(4):", s)  # {1, 3}
