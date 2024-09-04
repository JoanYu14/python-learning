import random

# random.random() – 傳回 [0.0, 1.0) 範圍(0.0~0.9999...)內的隨機浮點數。
print(random.random())

# random.randrange(start, stop[, step]) – 傳回從 range(start, stop, step) 中隨機選取的整數。開始、停止和步長都是整數。步驟是可選的。
print(random.randrange(0, 101))  # 隨機return 0~101(不含101)間的一個整數
for i in range(10):
    print(
        random.randrange(10, 20, 3)
    )  # 隨機從10~20間取整數，但都是10開始到20間隔3的數(10,13,16,19)


# random.randint(a, b) – 傳回一個隨機整數 N，使得 a <= N <= b； a、b均為整數。randrange(a, b+1) 的可互換。
print(random.randint(0, 100))  # 隨機return 0~101(不含101)間的一個整數
