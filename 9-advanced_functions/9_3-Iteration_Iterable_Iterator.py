# 如何使一個class可迭代
# === iterable => (1) 可迭代(iterable) object是一個具有__iter__  method的object，該method return 迭代器(iterator)
# 任何generator(生成器)都是iterator
class Something:
    def __iter__(self):
        yield 5
        for x in range(1, 4):
            yield x


s = Something()
print(s)  # <__main__.Something object at 0x0000026F1DB0F400>

# iter() 函數是 Python 中的一個內置函數，用於將可迭代對象轉換為迭代器。
# 這使得我們可以使用迭代器的功能，比如在循環中逐個訪問可迭代對象的元素。
print(iter(s))  # <generator object Something.__iter__ at 0x0000021082559510>

for i in s:
    print(i)
# 5
# 1
# 2
# 3


# === iterable => (2) __getItem__()
class Building(object):
    def __init__(self, floors):
        # 初始化方法，創建一個包含 None 的列表，長度為 floors
        # 用於存儲每層樓的數據
        self.__floors = [None] * floors

    def __setitem__(self, floor_number, data):
        # 定義索引賦值操作，例如 building1[0] = "Reception"
        # 將數據 data 設置到對應樓層（索引）的列表中
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        # 定義索引訪問操作，例如 building1[0]
        # 返回對應樓層（索引）的數據
        return self.__floors[floor_number]


# 創建一個 Building 對象，該對象有 4 層樓
building1 = Building(4)

# 使用 __setitem__ 方法設置每層樓的數據
building1[0] = "Reception"  # 第 0 層是 Reception
building1[1] = "ABC Corp"  # 第 1 層是 ABC Corp
building1[2] = "DEF Inc"  # 第 2 層是 DEF Inc
# 第 3 層未設置，保持 None（默認值）

# 使用 for 循環迭代 building1 對象，這是因為它實現了 __getitem__ 方法
# Python 將從索引 0 開始調用 __getitem__ 方法，直到超出索引範圍
for thing in building1:
    print(thing)  # 順序打印每層樓的內容，依次是 Reception, ABC Corp, DEF Inc, None
# Reception
# ABC Corp
# DEF Inc
# None


# ========== iterator ==========
# iterator是iterable的子集合
# 所以一個iterator一定是iterable，但一個iterable不一定是iterator
# 要檢查一個iterable是否為iterator就只要去檢查是否有實作__iter__ method與__next__ method。
lst1 = ["A", "B", "C"]
# dir() 函式用於列舉對象的所有屬性和方法。這包括對象的內建屬性、方法以及自定義的屬性和方法
print("__iter__" in dir(lst1))  # True
print("__next__" in dir(lst1))  # False
# List不是iterator，但為iterable

# __iter__() return一個iteraor
print("__iter__" in dir(iter(lst1)))  # True
print("__next__" in dir(iter(lst1)))  # True


# for i in iterable真正做的事
# step1. iter(iterable)得到一個iterator
# step2. 對iterator做next function => next(iterator)，這樣就會去抓到iterator的下一個值是甚麼
list_iterator = iter(lst1)
print(next(list_iterator))  # A，因為lst1的第1項是A
print(next(list_iterator))  # B，因為lst1的第2項是B
print(next(list_iterator))  # C，因為lst1的第3項是C

# line81~84的code就是這個for loop背後執行的動作
for i in lst1:
    print(i)

# print(next(list_iterator))  # Error:StopIteration


# === 怎麼自製一個iterator ===
class Myiterator:
    def __init__(self, max_num):
        # 初始化方法，設定迭代的最大數字（不包括 max_num 本身）和起始索引
        self.max_num = max_num
        self.index = 0

    def __iter__(self):
        # __iter__ 方法使得 Myiterator 對象可以被迭代
        # 返回 self，表示這個對象本身就是一個迭代器
        return self

    def __next__(self):
        # __next__ 方法定義了迭代過程中的每一步
        # 如果 index 小於 max_num，返回當前 index，並將 index 加 1
        if self.index < self.max_num:
            value = self.index
            self.index += 1
            return value
        else:
            # 如果 index 達到或超過 max_num，重設 index 並引發 StopIteration 異常，結束迭代
            self.index = 0
            raise StopIteration


# 創建一個 Myiterator 實例，設定最大數字為 5
iterator_item = Myiterator(5)

# 使用 for 循環來迭代 iterator_item
# for 循環會自動處理 StopIteration 異常，當異常被引發時，循環結束
for i in iterator_item:
    print(i)
# 預期輸出：
# 0
# 1
# 2
# 3
# 4
