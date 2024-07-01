# 寫一個名為「printEvery3」的函數，印出整數 1、4、7、10、...、88。
def printEvery3(num):
    for i in range(1,num+1,3):
        print(i)

printEvery3(88)