# 1. build-in nameSpace
# __builtins__模組
# 每次我們執行 Python 程式碼時，Python 解釋器都會自動導入一個 __builtins__module。
# 此模組包含Python內建函數，例如len()、int()、range()、str()等。
# __builtins__模組也是object

print(__builtins__)  # <module 'builtins' (built-in)>

string1 = "Hello"
print(__builtins__.len(string1))  # 5

# 在Python中，dir() 函數用於列出指定對象的屬性和方法。
# 當你使用 print(dir(Student)) 這個語句時，它將打印出 Student 這個對象（或者是類）的所有屬性和方法的列表。
print(dir(__builtins__))
# print(help(dir))
# dir([object]) -> 字串列表

# 2. global nameSpace
# 全域命名空間(global namespace)包含在主程式層級定義的任何名稱以及我們導入的所有模組。
# Python 提供了名為 globals()的內建函數，可讓您存取全域空間字典(global nameSpcae dictionary)。
print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024972876CD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\22300711\\Desktop\\python_learning\\7-modules_and_packages\\7_4-namespace\\try.py', '__cached__': None,
#  'string1': 'Hello'}

# 3. local nameSpace
# 局部命名空間(local namespace)包括函數內的本地名稱。局部命名空間是在呼叫函數時創建的，並且僅持續到函數返回或終止為止。
print("=========")
print(locals())
# 在這裡呼叫locals其實就是global命名空間
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000295AAB66CD0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\22300711\\Desktop\\python_learning\\7-modules_and_packages\\7_4-namespace\\try.py', '__cached__': None,
# 'string1': 'Hello'}


def sayLocals():
    a = 1
    b = 2
    # {'a': 1, 'b': 2}
    print(locals())


print("=========")
sayLocals()
# Python是用LEGB規則來找variable
# 1. Local：當前函數內的局部作用域。
# 2. Enclosing：嵌套函數的外部函數的作用域。
# 3. Global：全局作用域，即模塊級別的變量。
# 4. Built-in：Python 的內建作用域。
# 如果你在程式碼中把__builtins__ module內部的method name重新定義賦值的話python就不會使用原本__builtins__ module內部的method
# 因為python最後才會去build-in namespace找，但是在這之前就已經被找到了
