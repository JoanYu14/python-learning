# 定義名為sayHi的function，有name parameter(一定要傳入)和helloWord parameter(預設為Hi)
# return為None
def sayHi(name,helloWord="Hi"):
    print(f'{helloWord}，我是{name}')

# sayHi() TypeError: sayHi() missing 1 required positional argument: 'name'
sayHi("Joan") # Hi，我是Joan
sayHi("Joan","Aloha") # Aloha，我是Joan
print(sayHi("Joan")) # None

def plusFun(num1,num2):
    """這個function用於將num1加上num2並回傳"""
    number = num1+num2
    return number

print(plusFun(1,2)) # 3
help(plusFun)
# Help on function plusFun in module __main__:

# plusFun(num1, num2)
#     這個function用於將num1加上num2並回傳