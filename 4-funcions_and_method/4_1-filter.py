# 單個可迭代對象
numbers = [1, 2, 3, 4, 5, 6]
def foundEven(x):
    return x%2==0
even_numbers = filter(foundEven, numbers)
print(list(even_numbers))  # 輸出: [2, 4, 6]

# 如果 function 為 None，則保留所有trusly value
values = [0, 1, False, True, [], [1, 2, 3]]
true_values = filter(None, values)
print(list(true_values))  # 輸出: [1, True, [1, 2, 3]]
