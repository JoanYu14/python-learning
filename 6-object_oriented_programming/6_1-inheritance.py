# Inheritance(繼承)
class People():
    # 紀錄有使用People class創建的object，child class創建的object也會新增
    people_dir = {}
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
        self.people_dir[name] = age # 新增people_dir中key為name的value為age
    
    def sleep(self):
        print(f"{self.name}在睡覺")
    
    def eat(self):
        print(f"{self.name}在吃東西")

    def introduction(self):
        print(f"名字:{self.name}，年齡:{self.age}，國家:{self.country}")

    @classmethod
    def get_people_dir(cls):
        print(cls.people_dir)

# 裡面放入要繼承的parent class
class Teacher(People):
    teacher_dir = {}
    def __init__(self,name,age,country,suject):
        #super是從離散數學中的superset(超集)來的
        #設A和B是兩個集合，如果A的任意一個元素都是B的元素，則稱A為B的子集（subset），稱B為A的超集（superset）
        #使用super的object來取代下面那個People object
        #super還會繼承parent class的method
        super().__init__(name,age,country) # 使用super的話就不用放self參數 
        #People.__init__(self,name,age,country) # 若用此方法的話會只繼承People的attribute，不繼承method
        self.suject = suject
        self.teacher_dir[name] = suject

    def teach(self):
        print(f"{self.name}正在教{self.suject}")

    # 這樣呼叫introduction method的時候就會執行這個而不是People class的introduction method
    def introduction(self):
        print(f"名字:{self.name}，年齡:{self.age}，國家:{self.country}，職業:{self.suject}老師")

    @classmethod
    def get_teacher_dir(cls):
        print(cls.teacher_dir)

class Student(People):
    student_dir = {}
    def __init__(self,name,age,country,major):
        super().__init__(name,age,country)
        self.major = major
        self.student_dir[name] = major

    @classmethod
    def get_student_dir(cls):
        print(cls.student_dir)
    
    
    def learn(self):
        print(f"{self.name}正在學習，他主修{self.major}")

teacher1 = Teacher("Jessice",26,"USA","English")
student1 = Student("John",21,"Japan","CS")
student2 = Student("Kevin",22,"Thailand","History")
person1 = People("Max",11,"Hongkong")

# Student與Tacher的method呼叫
student1.learn()
teacher1.teach()

# Teacher的class有定義introduction method，覆蓋People這個parent class的introduction method
teacher1.introduction()
# Student中沒有覆寫從People繼承的introduction method
student1.introduction()
person1.introduction()

# 呼叫classmethod，綁定在Class本身
# 使用classmethod的好處是如果method中不會用到要自定義的attribute的話，每個object都是得到固定的結果
# 那將method定義為classmethod能減少空間用量
# 取得紀錄Student創建的obejct的dictionary
student1.get_student_dir()
# 取得紀錄Teacher創建的obejct的dictionary
teacher1.get_teacher_dir()

# 呼叫parent class People的classmethod
teacher1.get_people_dir()
student1.get_people_dir()

# 呼叫從parent class People繼承的method
teacher1.sleep()


