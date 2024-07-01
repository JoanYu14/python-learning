# 編寫一個名為「findSmallCount」的函數
# 該函數接受一個整數列表和一個整數作為輸入，並傳回一個整數，指示列表中有多少元素小於輸入整數。
# *num_list
# def findSmallCount(num,*num_tuple):
#     print(num_tuple)
#     small_than_count = len(list(filter(lambda x:x<int(num),num_tuple)))
#     return small_than_count

def findSmallCount(num,num_list):
    # small_than_count = len(list(filter(lambda x:int(x)<num,num_list)))
    # 使用列表推導式從 num_list 中篩選出所有滿足條件 int(x) < num 的元素 x，並計算這些元素的個數。
    small_than_count = len([x for x in num_list if int(x)<num])
    
    # 以下寫法較不佔空間
    # small_than_count = 0
    # for x in num_list:
    # if int(x) < num:
    #     small_than_count += 1
    return small_than_count


input_num = int(input("請輸入作為標準的整數:"))
input_nums = input("請輸入要比較的整數，以空格分開:").split(" ")
print(f'有{findSmallCount(input_num,input_nums)}個數字小於{input_num}')