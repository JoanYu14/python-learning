# 單個可迭代對象
def square(x):
    return x**2
numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(squared) # <map object at 0x000002B271493FA0>
print(list(squared))  # 輸出: [1, 4, 9, 16]

# 多個可迭代對象
def addition(x,y):
    return x+y
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6,4,5,6]
# addtion的第一個argument為numbers1的元素，第二個argument為numbers2的元素，若兩者長度不同則以短的為主
added = map(addition, numbers1, numbers2)
print(list(added))  # 輸出: [5, 7, 9]