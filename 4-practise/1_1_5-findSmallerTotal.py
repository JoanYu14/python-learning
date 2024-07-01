# 編寫一個名為「findSmallerTotal」的函數
# 該函數接受一個整數列表和一個整數作為輸入，並傳回列表中小於輸入整數的所有元素的總和。
def findSmallerTotal(num,num_list):
    # 使用生成器推導式創建名為small_than_list的生成器
    # 生成器表達式: int(x) for x in num_list if 條件: int(x) < num
    # 意思是從 num_list 中選取每個元素 x，如果 int(x) 小於 num 的話，則產生 int(x) 這個值。
    small_than_num_generator = (int(x) for x in num_list if int(x)<num)
    total = 0
    # 遍歷生成器
    for i in small_than_num_generator:
        total+=i
    return total


input_num = int(input("請輸入作為標準的整數:"))
input_nums = input("請輸入要比較的整數，以空格分開:").split(" ")
print(f"小於{input_num}的數字總和為:{findSmallerTotal(input_num,input_nums)}")