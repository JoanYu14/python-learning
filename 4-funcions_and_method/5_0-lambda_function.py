# 基本例子
add = lambda x, y: x + y
print(add(2, 3))  # 輸出: 5

# 排序使用 lambda 表達式
points = [(1, 2), (4, 1), (5, -1), (2, 3)]
# sort 方法用來排序列表 points。
# key=lambda point: point[1] 指定了排序的鍵值（key）。
# 這裡的 Lambda 函式 lambda point: point[1] 接受一個參數 point，並返回 point 元組的第二個元素（即 point[1]），這樣就根據每個元組的第二個元素來進行排序。
points.sort(key=lambda point: point[1])
print(points)  # 輸出: [(5, -1), (4, 1), (1, 2), (2, 3)]

# 與map一起用
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 輸出: [1, 4, 9, 16, 25]

# 與filter一起用
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 輸出: [2, 4, 6]


# 使用 lambda 函數來定義一個匿名函數，並在定義時即呼叫它，傳入 testNum 作為參數
# lambda 函數的語法為 lambda parameters: expression
# 這裡的參數是 testNum，表達式是 testNum * 2，即返回 testNum 的兩倍
result = (lambda testNum: testNum * 2)(2)
# 印出結果
print(result)  # 輸出: 4

# 兩個parameter
result = (lambda num1,num2:(num1+num2,num1-num2))(2,4)
print(result)
