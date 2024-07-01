# global variable(全域變數)、local variable(局部變數) =============================
# copy by value ========================
a = 5 # gloabal variable
def changeNum(num):
    # num = a => 這是python偷偷做的是把a copy到num，且是copy by value
    num = 10 #num只在changeNum函數中可存取

changeNum(a)
# 還是5，因為changeNum中的num雖然是copy a，但由於integer是copy by value所以不會去變動原本a的值
print(a)

# copy by reference ===================
list1 = [1,2,3,4]
def changeList(list):
    # list = a => 這是python偷偷做的是把a copy到num，且是copy by "reference"
    # 由於是copy by reference，所以list與list1其實是指向同一個位置，因此這個操作也會變動list1[0]的值
    list[0] = 100 

changeList(list1)
print(list1) # [100, 2, 3, 4]

# 在function中更改global variable的方法
# global key word: 在函數內部使用 global 關鍵字聲明一個變量時，該變量指向的是全局範圍（即模塊級別）的變量，而不是創建一個新的局部變量。
x = 10
def changeGlobalVarx(plusValue):
    global x 
    x += plusValue # x是global varaible，plusValue是local variable

changeGlobalVarx(100)
print(x) # 110