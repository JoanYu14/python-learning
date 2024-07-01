def example_function(*args, **kwargs):
    print("非關鍵字參數:")
    for arg in args:
        print(arg)

    print("\n關鍵字參數:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, 3, name="Alice", age=30, job="Engineer")
# 輸出：
# 非關鍵字參數:
# 1
# 2
# 3
#
# 關鍵字參數:
# name: Alice
# age: 30
# job: Engineer