# 寫一個名為「table」的函數
# 它接受輸入 n，並印出 n x 1 到 n x 9

def table(num):
    for number in range(1,num+1):
        for value in range(1,10):
            print(f'{number} X {value} = {number*value}')
            
input_num = int(input("請輸入n: "))
table(input_num)      
