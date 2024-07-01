# 1. __len__
#作用：定義對象的長度。通常用於內建函數 `len()` 的支持。
#說明：當對象被傳遞給 `len()` 函數時，Python 解釋器會調用該對象的 `__len__` 方法來獲取對象的長度。
class MyClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_obj = MyClass([1, 2, 3, 4, 5])
print(len(my_obj))  # Output: 5

# 2. __str__
# 作用：返回對象的友好、可讀性較高的字符串表示形式。
# 說明：`str()` 函數會嘗試調用對象的 `__str__` 方法來獲取對象的字符串表示形式。通常用於用戶友好的輸出。
# 後面直接print(instanceName)的時候就會去呼叫__str__函數取得此函數的return值並印出
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass instance with name: {self.name}"

my_obj = MyClass("Alice")
print(my_obj)  # Output: MyClass instance with name: Alice

# 3. __repr__
# 作用：返回對象的官方字符串表示形式（通常是可以用來重新建立對象的表示形式）。
# 說明：`repr()` 函數會調用對象的 `__repr__` 方法來獲取對象的官方字符串表示形式。通常用於開發和調試中。
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyClass(name='{self.name}')"

my_obj = MyClass("Alice")
print(repr(my_obj))  # Output: MyClass(name='Alice')

# 4. __add__
# 作用：定義對象的加法行為。
# 說明：當兩個對象使用 `+` 運算符進行相加時，Python 解釋器會調用左邊對象的 `__add__` 方法，並將右邊對象作為參數傳遞給該方法。
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)  # Output: 4 6

# 5. __gt__、__ge__、__lt__、__le__
# 作用：分別定義對象的大於、大於等於、小於、小於等於比較行為。
# 說明：這些方法允許你定義對象之間的比較操作，例如使用 `>`、`>=`、`<`、`<=` 等運算符。這些方法返回 `True` 或 `False`。
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 > p2)   # Output: False
print(p1 >= p2)  # Output: False
print(p1 < p2)   # Output: True
print(p1 <= p2)  # Output: True






