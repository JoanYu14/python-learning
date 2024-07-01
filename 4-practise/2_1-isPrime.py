# 寫一個名為「isPrime」的函數
# 它接受一個整數作為輸入，並傳回一個布林值，指示輸入數字是否為質數。
def isPrime(num):
    # 創建一個列表，包含從 2 到 num-1 之間所有能整除 num 的數字。
    not1_and_self_factors = [x for x in range(2, num) if num % x == 0]
    
    # 輸出除了 1 和自身以外的因數列表。
    print(f'{num}除了1與自己的因數有:{not1_and_self_factors}')

    # 如果 not1_and_self_factors 列表不為空，則表示 num 有其他因數，因此不是質數，返回 False。
    if len(not1_and_self_factors):
        return False
    else:
        # 如果 not1_and_self_factors 列表為空，則表示 num 只能被 1 和自身整除，是質數，返回 True。
        return True

# 請使用者輸入一個整數，並呼叫 isPrime 函數來判斷它是否為質數。
input_num = int(input("請輸入一個整數: "))
print(f'{input_num}是否為質數: {isPrime(input_num)}')
