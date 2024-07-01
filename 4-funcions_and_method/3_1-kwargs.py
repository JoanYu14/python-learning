def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=30, job="Engineer")
# 輸出：
# name: Alice
# age: 30
# job: Engineer