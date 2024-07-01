# 寫一個函數來檢查列表是否包含 007 的子序列
# print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False

def spyGame(num_list):
    count_of_0 = num_list.count("0")
    count_of_7 = num_list.count("7")
    if (count_of_0>=2) and (count_of_7>=1):
        return True
    else:
        return False

input_nums = input("請輸入list，以空格分開:").split(" ")
print(f"list{input_nums}是否有007元素:{spyGame(input_nums)}")