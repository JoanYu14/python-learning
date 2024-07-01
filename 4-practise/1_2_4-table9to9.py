# 寫一個名為「table9to9」的函數來列印乘法表：
def table9to9():
    for i in range(1,10):
        for j in range(1,10):
            print(f'{i} X {j} = {i*j}')

table9to9()