# 寫一個名為「pyramid」的函數
# 它接受一個整數作為輸入，並以以下模式列印金字塔：
# pyramid(1);
# *
# pyramid(2);
#  *
# ***
# pyramid(4); 
#    *
#   ***
#  *****
# *******
def pyramid(num):
    # 使用 enumerate 函數遍歷 range(num, 0, -1)，產生從 num 到 1 的數字序列，並同時獲取索引 counter 和值 i。
    for counter, i in enumerate(range(num, 0, -1)):
        # 計算每一行開頭的空格數，等於 i-1，因為最下層開頭不需要空格，倒數第二層開頭需要 1 個空格，依此類推。
        left_space = i - 1
        # 計算每一行星號的個數，等於 (counter + 1) * 2 - 1，即每一行星號數量呈現遞增的狀態。
        star_count = (counter + 1) * 2 - 1
        # 使用空格和星號打印金字塔的每一行，left_space * " " 表示空格，star_count * "*" 表示星號。
        print(left_space * " " + star_count * "*")

# 讓使用者輸入金字塔的層數
input_num = int(input("請輸入層數: "))
# 呼叫 pyramid 函數，根據輸入的層數打印金字塔
pyramid(input_num)
