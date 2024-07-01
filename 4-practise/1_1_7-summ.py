# 寫一個名為「summ」的函數
# 它接受一個數字列表，並傳回輸入列表中所有元素的總和。
def summ(num_list):
    # 使用生成器表達式從 num_list 中創建 num_list_generator 生成器，
    # 將 num_list 中的每個元素 x 轉換為整數後逐個生成。
    num_list_generator = (int(x) for x in num_list)
    total = 0
    for i in num_list_generator:
        total+=i
    return total

input_num_list = input("請輸入要加總的所有數字，以空格分開:").split(" ")
print(f'這些數字的總和為{summ(input_num_list)}')
