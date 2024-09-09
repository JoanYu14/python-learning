# 1. type()
# type(object) – 傳回作為參數傳遞的參數的類別類型。
print(type(123))  # <class 'int'>
print(type("123"))  # <class 'str'>
print(type(123) == type("123"))  # False


# 2. isinstance()
# isinstance(object, class) – 傳回一個布林值，指示該物件是否屬於該類別或從該類別繼承。
class A:
    pass


class B(A):
    pass


class C(B):
    pass


a = A()
b = B()
c = C()
print(isinstance(c, C))  # True
print(isinstance(c, B))  # True
print(isinstance(c, A))  # True
print(isinstance(a, A))  # True
print(isinstance(a, B))  # False
print(isinstance(a, C))  # False

# isusbclass(classA, classB) - 傳回一個布林值，指示 2 classA 是否是 classB 的子類別。請注意，一個類別是其自身的子類別。
# 這個概念來自集合論──任何集合都是它自己的子集。
print(issubclass(A, A))  # True
print(issubclass(A, B))  # False
print(issubclass(A, B))  # False
print(issubclass(C, C))  # True
print(issubclass(C, B))  # True
print(issubclass(C, A))  # True
