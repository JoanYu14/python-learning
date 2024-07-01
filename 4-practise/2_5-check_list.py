# 給定一個整數列表，如果列表中 3 旁邊包含 3，則傳回 True。
# print(has_33([1, 5, 7, 3, 3])) # True
# print(has_33([])) # False
# print(has_33([4, 3, 2, 1, 0])) # False
def check_list_next(num,check_list):
    # 因為只需要最後的index右邊沒有元素了，所以遍歷list從index:0到最後的index-1就能check完了
    # for index,value in enumerate(check_list[0:len(check_list)-1]):
    #     return
    for i in range(len(check_list)-1):
        if (check_list[i]==str(num)) and (check_list[i+1]==str(num)):
            return True
    return False
    

check_num = int(input("請輸入要確認的數字:"))
input_nums = input("請輸入list，以空格分開:").split(" ")
print(f"list{input_nums}是否有{check_num}旁邊包含{check_num}:{check_list_next(check_num,input_nums)}")