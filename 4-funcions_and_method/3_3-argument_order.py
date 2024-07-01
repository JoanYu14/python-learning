# argument定義順序
# 普通參數 => 默認參數 => args => *kwargs
def example_function(param1, param2="default", *args, **kwargs):
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    print("非關鍵字參數:")
    for arg in args:
        print(arg)

    print("關鍵字參數:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function("value1", "value2", 3, 4, 5, name="Alice", age=30)
# 輸出：
# param1: value1
# param2: value2
# 非關鍵字參數:
# 3
# 4
# 5
#
# 關鍵字參數:
# name: Alice
# age: 30

