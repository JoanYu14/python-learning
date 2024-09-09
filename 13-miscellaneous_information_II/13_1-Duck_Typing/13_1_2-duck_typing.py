# 鴨子類型是指 Python 確定物件是否是操作所需類型的方法，重點關注其介面而不是其類型。
# 例如，如果某個操作需要迭代器，則所使用的物件不需要是任何特定迭代器的子類別或根本不需要是任何迭代器。
# 重要的是用作迭代器的物件能夠以預期的方式產生一系列物件。相較之下，像 Java 這樣的語言強制執行更嚴格的繼承規則。

# sorted function使用了鴨子類型(Duck Typing)的原理
# Python 的 sorted 函數並不直接依賴於傳入對象的具體類型，而是依賴於對象是否能夠進行排序操作。
# sorted 函數的目的是對一個可迭代對象（如列表、元組或其他容器）進行排序
# sorted 函數本身並不關心傳入的對象是否是 list、tuple 或任何具體類型。
# 只要這個對象能夠被迭代（即它實現了迭代協議），並且其元素能夠比較大小（即可以使用 <、> 等比較運算符），sorted 函數就能正常工作。
print(sorted(["foo", "bar", "fox"]))  # ['bar', 'foo', 'fox']
print(sorted({"foo", "bar", "fox"}))  # ['bar', 'foo', 'fox']
print(sorted({"key1": "foo", "key2": "bar", "key3": "fox"}))  # ['key1', 'key2', 'key3']
print(sorted("foobarfox"))  # ['a', 'b', 'f', 'f', 'o', 'o', 'o', 'r', 'x']


# 自訂duck typing的function
# 這個function並不會去檢查參數的型別，只要x,y可以相加就好
def calculate(x, y, z):
    return (x + y) * z


print(calculate(2, 2, 3))  # 12
print(calculate("foo", "bar", 3))  # foobarfoobarfoobar
print(
    calculate([1, 2], [3, 4], 5)
)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
