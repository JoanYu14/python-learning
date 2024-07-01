# 寫一個名為「inversePyramid」的函數
# 將金字塔倒置繪製。
# inversePyramid(4);
# *******
#  *****
#   ***
#    *
def inversePyramid(num):
    # 使用 enumerate 函數遍歷 range(num, 0, -1)，產生從 num 到 1 的數字序列，並同時獲取索引 counter 和值 i。
    for counter, i in enumerate(range(num, 0, -1)):
        left_space = counter
        star_count = (num-counter) * 2 - 1
        print(left_space * " " + star_count * "*")

# 讓使用者輸入金字塔的層數
input_num = int(input("請輸入層數: "))
# 呼叫 inversePyramid 函數，根據輸入的層數打印金字塔
inversePyramid(input_num)