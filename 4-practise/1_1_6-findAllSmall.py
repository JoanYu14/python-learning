# 編寫一個名為「findAllSmall」的函數
# 該函數將一個整數列表和另一個整數作為輸入，並傳回一個整數列表，其中包含小於輸入整數的所有元素。
def findAllSmall(num,num_list):
    # 使用列表推導式從 num_list 中創建 small_than_num_list 列表，其中包含所有滿足條件 int(x) < num 的元素 x。
    small_than_num_list = [x for x in num_list if int(x)<num]
    return small_than_num_list


input_num = int(input("請輸入作為標準的整數:"))
input_nums = input("請輸入要比較的整數，以空格分開:").split(" ")
print(f"小於{input_num}的數字列表為:{findAllSmall(input_num,input_nums)}")