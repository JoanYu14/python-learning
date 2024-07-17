# __hash__():在使用這個 Robot Class時，__hash__() 方法會自動被調用，這樣你就可以將 Robot 對象用作字典的鍵或者放入集合中。


class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 定義一個private method(私有函數)__key，return包含name,age,address的tuple
    def __key(self):
        return (self.name, self.age, self.address)

    # 實行hash fucntion，__hash__() method是 Python 中用於定義對象 hash 值的特殊方法。
    # 這裡，__hash__ method使用 hash 函數計算了 self.__key() 的 hash 值。這裡的 self.__key() 調用了上面定義的 __key 方法
    # 因此每個 Robot 對象的 hash 值將基於其 name、age 和 address 的tuple計算而來。
    def __hash__(self):
        return hash(self.__key())

    # self會放入自己，other則是放入比較對象
    def __eq__(self, other):
        # 傳回物件是否是類別或其子類別的實例。也就是會去檢查other是否為Robot class或Robot的child class所創建的instance
        if isinstance(other, Robot):
            # 去比較他們要去hash的tuple有沒有一樣，若是一樣的話代表他們是一模一樣的
            return self.__key() == other.__key()

        # NotImplemented。這個返回值的目的是告訴 Python 解釋器說，對於這個比較操作，當前類別無法處理這個對象類型的比較。
        return NotImplemented


# 創建幾個 Robot 對象
robot1 = Robot("Robot1", 5, "123 Main St")
robot2 = Robot("Robot2", 3, "456 Elm St")
robot3 = Robot("Robot3", 7, "789 Oak St")
robot4 = Robot("Robot3", 7, "789 Oak St")

# 創建一個字典，使用 Robot 對象作為鍵
robots_dict = {robot1: "First Robot", robot2: "Second Robot", robot3: "Third Robot"}

# 使用 Robot 對象查找字典中的值
# 當我們使用 robot1 或 robot2 來查找字典中的值時，Python 會使用 __hash__() 方法計算它們的 hash 值，並根據這個 hash 值來快速查找對應的值。
print(robots_dict[robot1])  # Output: First Robot
print(robots_dict[robot2])  # Output: Second Robot

# 創建一個集合，包含多個 Robot 對象
robots_set = {robot1, robot2, robot3, robot4}

# 遍歷集合中的每個元素
for robot in robots_set:
    print(f"Robot name: {robot.name}, Age: {robot.age}, Address: {robot.address}")


# 沒加__eq__()之前的結果，可以看到有兩個Robot3，但其實robot3與robot4是一模一樣的
# Robot name: Robot2, Age: 3, Address: 456 Elm St
# Robot name: Robot3, Age: 7, Address: 789 Oak St
# Robot name: Robot3, Age: 7, Address: 789 Oak St
# Robot name: Robot1, Age: 5, Address: 123 Main St

# 加了__eq__()後的結果，由於會使用__eq__()去比較兩個instance的key tuple是否相同，所以robot3與robot4變成一筆了
# Robot name: Robot2, Age: 3, Address: 456 Elm St
# Robot name: Robot3, Age: 7, Address: 789 Oak St
# Robot name: Robot1, Age: 5, Address: 123 Main St
