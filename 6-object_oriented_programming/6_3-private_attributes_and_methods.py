# Private Attributes and Methods 私有屬性與函數
# private(私有)意味著attribute屬性或method方法僅有class內部可用，而不對類別的外部可用。
# 代表class A外部並不能直接取用私有的attribute與method，不管是不是由People()創建的object

class People():
    __people_list = []
    __allaow_change_country_list = ["Japan","USA","Thailand"]
    def __init__(self,name,age):
        self.name = name
        # age為private attribute
        self.age = age
        self.__country = "USA"
        self.__people_list.append({name:age})
    
    def get_age(self):
        print(f"{self.name}的年齡是{self.age}")
    
    def geet(self):
        print(f"{self.name}打招呼")

    # 可以透過此method來限制__country被更改為任意值，這就是為何要把屬性私有化
    # 這就是setter
    def change_country(self,input_country):
        if (input_country not in self.__allaow_change_country_list):
            print(f"您無法更改為{input_country}")
        else:
            self.__country = input_country
        

    #get_country是定義在People class內部的，所以此method內部可以取用People的private attribute
    #所以child class可以透過此method來得到__country，這就是getter
    def get_country(self):
        print(f'{self.name}來自{self.__country}')
    
    def __get_people_list(self):
        print(f'目前有{len(self.__people_list)}個人，列表:{self.__people_list}')

    @classmethod
    def public_get_people_list(cls):
        cls.__get_people_list(cls)

class Student(People):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    
    def learn(self):
        print(f'{self.name}正在讀{self.major}')

student1 = Student("John",25,"CS")

# 無法直接取用parent class People的__country屬性
#print(student1.__country) # AttributeError: 'Student' object has no attribute '__country'

# 雖然__country是People的private attribute，但get_country並不是private method
# 並且get_country是定義在People class內部的，所以此method內部可以取用People的private attribute
student1.get_country() # John來自USA
# 透過從People繼承change_country method還是可以去更改private attribute
student1.change_country("Japan") # 將student1的__country改為Japan
student1.get_country() # John來自Japan
student1.change_country("Vietnam") # 您無法更改為Vietnam
student1.get_country()

# People.__get_people_list() # AttributeError: type object 'People' has no attribute '__get_people_list'
# 即使是class本身也無法直接取用private method or attribute
# public_get_people_list()這個class method會去呼叫__get_people_list()這個private method
student1.public_get_people_list() # 目前有1個人，列表:[{'John': 25}]
