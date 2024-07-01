def greet():
    print("greet")

    def hello1():
        print("hello1")
        hello2()


    def hello2():
        # hello1() # hello2與hello1在同一個scope
        print("hello2")
        # hello2_2() UnboundLocalError: local variable 'hello2_2' referenced before assignment
        def hello2_2():
            print("hello2_2")
        hello2_2()

    hello1()
    # hello2_2()無法找到

greet()
# greet
# hello1
# hello2
# hello2_2

# ======= LEGB規則 =======
# 1. Local：當前函數內的局部作用域。
# 2. Enclosing：嵌套函數的外部函數的作用域。
# 3. Global：全局作用域，即模塊級別的變量。
# 4. Built-in：Python 的內建作用域。

name = "Joan"

def greet2():
    name="Kevin"
    def greet2_1():
        print(name) # LEGB規則"2" => Enclosing：嵌套函數的外部函數的作用域。 => 從greet2的name變數來的(Kevin)
    greet2_1()

def hello2():
    # LEGB規則"3" => 從global中的name變數來的(Joan) => 全局作用域中的函式通常不具有嵌套作用域。
    # LEGB規則"4" => print()這個函數則是從Built-in：Python 的內建作用域。
    print(name) 

greet2() # Kevin
hello2() # Joan