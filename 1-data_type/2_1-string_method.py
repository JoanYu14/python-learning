# 字符串method示例
# len()
s = "Hello, world!"
print("len(s):", len(s))  # 13

# int()
s = "123"
print("int(s):", int(s))  # 123

# float()
s = "123.45"
print("float(s):", float(s))  # 123.45

# str()
x = 123
print("str(x):", str(x))  # "123"

# upper()
s = "Hello, world!"
print("s.upper():", s.upper())  # "HELLO, WORLD!"
print(s) # Hello, world!，因為python不會改變原本的s字串

# lower()
s = "Hello, WORLD!"
print("s.lower():", s.lower())  # "hello, world!"

# isupper()
s = "HELLO"
print("s.isupper():", s.isupper())  # True
s = "Hello"
print("s.isupper():", s.isupper())  # False
print("s.upper().isupper():",s.upper().isupper()) # True

# index()
s = "Hello, world!"
print("s.index('world'):", s.index("world"))  # 7
#print(s.index("a"))  # ValueError: substring not found

# replace()
s = "Hello, world!"
print("s.replace('world', 'Python'):", s.replace("world", "Python"))  # "Hello, Python!"

# split()
s = "Hello, world! Welcome to Python."
print("s.split():", s.split())  # ['Hello,', 'world!', 'Welcome', 'to', 'Python.']
print("s.split('!'):",s.split("!")) # ['Hello, world', ' Welcome to Python.']


# list()
s = "Hello"
print("list(s):", list(s))  # ['H', 'e', 'l', 'l', 'o']

# format()
s = "Hello, {}!"
print("s.format('world'):", s.format("world"))  # "Hello, world!"
print("Hello, {name}".format(name="Joan")) # Hello, Joan
print("{greet}, {name}".format(name="Joan",greet="Hi!")) # Hi!, Joan，這是以參數的方式format
print("{1},{0}".format("Joan","Aloha")) # Aloha,Joan，這是以index的方式format
print("{},{},{}".format(1,2,3)) # 1,2,3，這是照順序format
print("{},{},{}".format(1,2,3,4)) #1,2,3
#print("{},{},{}".format(1,2)) # IndexError: Replacement index 2 out of range for positional args tuple

# fstring
# python3.6引入
name = "Joan"
print(f"Hello, {name}") # Hello, Joan
print(f"1+2={1+2}") # 3

# count()
s = "Hello, world! Welcome to the world of Python."
print("s.count('world'):", s.count("world"))  # 2

# find()
s = "Hello, world!"
print("s.find('world'):", s.find("world"))  # 7
print("s.find('Python'):", s.find("Python"))  # -1

# startswith()
s = "Hello, world!"
print("s.startswith('Hello'):", s.startswith("Hello"))  # True
print("s.startswith('world'):", s.startswith("world"))  # False

# endswith()
s = "Hello, world!"
print("s.endswith('world!'):", s.endswith("world!"))  # True
print("s.endswith('Hello'):", s.endswith("Hello"))  # False

# isalpha() => 如果字串至少有一個字元且所有字元都是字母則傳回 True，否則傳回 False。
s= "!===cc"
print(f'{s}字串中是否有特殊符號:{not s.isalpha()}')

