# 編寫一個名為“findMin”的函數
# 它將列表作為輸入，並傳回輸入列表中的最小元素。
def findMin(lst):
    lst = sorted(lst)
    return lst[0]

input_nums = input("請輸入整數，以空格分開:").split(" ")
input(f"{input_nums}中最小的是{findMin(input_nums)}")