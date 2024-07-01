# 1-變數值互換
# 1-1其他語言
a = 1
b = 2
temp = b
b = a
a = temp
print(f'a為:{a}，b為:{b}')
# 1-2 pythonic
a1 = 1
b1 = 2
b1,a1=a1,b1
print(f'a1為:{a1}，b1為:{b1}')

# 2-比較
# 2-1其他語言
num = 50
if num>20 and num<100:
    print("num介於20~100間")
# 2-2 pythonic
if 20<num<100:
    print("num介於20~100間")

# 3-判斷
# 3-1其他語言
fruit = input("請輸入一個水果:")
if (fruit=="蘋果") or (fruit=="香蕉"):
    print("你要的水果有販售")
else:
    print("你要的水果目前沒貨")
# 3-2 pythonice
if fruit in ("蘋果","香蕉"):
    print("你要的水果有販售(pythonic)")
else:
    print("你要的水果目前沒貨(pythonic)")  