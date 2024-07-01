# 寫一個名為「stars2」的函數，它會以以下模式列印星星層：
# stars2(1);
# # *
# stars2(2);
# # *
# # **
# # *
# stars2(3);
# # *
# # **
# # ***
# # **
# # *
# stars2(4);
# # *
# # **
# # ***
# # ****
# # ***
# # **
# # *

def stars2(num):
    for i in range(1,(num*2)):
        if i <= num:
            print("*"*i)
        else:
            print("*"*(num-(i-num)))

input_num = int(input("請輸入層數: "))
stars2(input_num)            