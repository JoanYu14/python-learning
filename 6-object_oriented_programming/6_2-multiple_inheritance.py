# Multiple Inhertance 多重繼承:
# 在 Java 和 JavaScript 中，不允許多重繼承。Python支援多重繼承，這意味著我們可以從多個父class繼承。



class E():
    def e_method(self):
        print("從E繼承的method")

class F():
    def f_method(self):
        print("從F繼承的method")

    def do_stuff(self):
        print("這是F class的de_stuff method")

# B會繼承E class與F class
class B(E,F):
    def b_method(self):
        print("從B繼承的method")


class C():
    def c_method(self):
        print("從C繼承的method")
    def do_stuff(self):
        print("這是C class的de_stuff method")

class G():
    def d_method(self):
        print("從G繼承的method")
    def do_stuff(self):
        print("這是G class的de_stuff method")

class D(G):
    def d_method(self):
        print("從D繼承的method")



class A(B,C,D):
    pass





a = A()
a.c_method()
a.b_method()
a.e_method()

# 順序 => F,C,G都有do_stuff method
# 方法解析順序（MRO）的基本原理採用深度優先的圖遍歷演算法。透過應用該演算法，我們將得到：
# A、B、E、F、C、D、G
a.do_stuff()

#如果無法確定MRO，我們可以使用Python內建：
#classname.mro()
print(A.mro()) # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.F'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.G'>, <class 'object'>]
# classname.__mro__
print(A.__mro__) # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.F'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.G'>, <class 'object'>)