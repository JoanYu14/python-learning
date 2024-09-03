# 定義一個名為 Robot 的類別
class Robot:
    # 使用 pass 表示這個類別目前沒有任何屬性或方法
    pass


# 創建 Robot 類別的一個實例，並將其賦值給 new_robot 變數
new_robot = Robot()

# 使用 print 函數來輸出 new_robot 變數的類型
# type(new_robot) 返回 new_robot 的類型，這裡應該是 <class '__main__.Robot'>
print(type(new_robot))  # <class '__main__.Robot'>


class Car:
    # 在class中，我們也可以定義描述
    """Car class是用於製作Car物件"""

    # 這是class attribute(類別屬性)，在所有這個class的instance(object)之間共享。這意味著如果你改變了類屬性，這個改變將會影響所有實例。
    element = ["鋼鐵", "橡膠"]

    #  __init()__ 此函數讓類別class初始化物件object的屬性(attributes)，也就是說當我們每次用class製作一個object的時候__init()__都會被執行
    # init就是constructor(建構函數)
    # 定義在init內部的屬性為instance attribute(實例屬性)也可稱為object attribute
    def __init__(self, input_name, input_brand):  # self指的是自己()
        self.name = (
            input_name  # 這個物件的name attribute為init函數中的input_name參數的值
        )
        self.brand = (
            input_brand  # 這個物件的brandattribute為init函數中的input_brand參數的值
        )
        # self.element = ["鋼鐵","橡膠"] 如果將這個固定的attribute設定在這裏的話每次使用Car創造新物件的話就都要再占用這個空間。但是所有的Car物件都有相同的element屬性

    # 定義名為turn的method
    # method的第一個參數一定是self
    def turn(self, direction):
        print(f"{self.name}在{direction}轉")

    def introduce(self):
        # bran與name是object(instance) attribute，element是class attribute
        print(f"這是一台{self.brand}的{self.name}，材料為:{self.element}")

    # 要定義static method一定要用@staticmethod
    @staticmethod
    # static method的第一個參數不用是self，但其實這樣的話如果我們要取得attribute的話就只能用hardcode的方式，較不好
    def intro():
        print("這是一台汽車")

    @classmethod
    def intro2(cls):
        print(f"汽車的原料有{cls.element}")


car1 = Car("XC90", "volvo")
car2 = Car("GLC", "Benz")
print(type(car1))  # <class '__main__.Car'>

# obejct(instance) attribute : 綁定在object的attribute，而非綁定在class上
# print(car1.__class__.name) # AttributeError: type object 'Car' has no attribute 'name'
print(
    f"car1的車名為:{car1.name}，品牌為:{car1.brand}"
)  # car1的車名為:XC90，品牌為:volvo
print(
    f"car1的class的描述為:{car1.__doc__}"
)  # Car class的描述為:Car class是用於製作Car物件

# class attribute
print(Car.element)  # ['鋼鐵', '橡膠']
print(car1.element)  # ['鋼鐵', '橡膠']
print(car1.__class__.element)  # ['鋼鐵', '橡膠']

# method，是綁定在object上，而非class上
# Car.trun() AttributeError: type object 'Car' has no attribute 'trun'
car1.turn("右")  # XC90在右轉
car2.turn("左")  # GLC在左轉
car1.introduce()  # 這是一台volvo的XC90，材料為:['鋼鐵', '橡膠']

# static method : 綁定在class上的method，也就是所有object共用這個method
car1.intro()
car1.__class__.intro()
car1.__class__.intro2()
