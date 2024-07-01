# 編寫一個名為「stars」的函數，以以下模式列印星星圖層：
# stars(1);
# # *
# stars(4);
# # *
# # **
# # ***
# # ****

def stars(num):
    for i in range(1,num+1):
        print("*"*i)

input_num = int(input("請輸入層數: "))
stars(input_num)