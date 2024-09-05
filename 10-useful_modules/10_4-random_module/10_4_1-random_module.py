import random

# random.random() – 傳回 [0.0, 1.0) 範圍(0.0~0.9999...)內的隨機浮點數。
print(random.random())

# random.randrange(start, stop[, step]) – 傳回從 range(start, stop, step) 中隨機選取的整數。開始、停止和步長都是整數。步驟是可選的。
print(random.randrange(0, 101))  # 隨機return 0~101(不含101)間的一個整數
for i in range(10):
    print(random.randrange(10, 20, 3))  # 隨機從10~20間取整數，但都隔3的數(10,13,16,19)


# random.randint(a, b) – 傳回一個隨機整數 N，使得 a <= N <= b； a、b均為整數。randrange(a, b+1) 的可互換。
print(random.randint(0, 100))  # 隨機return 0~101(不含101)間的一個整數

# random.seed()
# seed() 函數用於保存隨機函數的狀態，以便在同一台機器或不同機器上（對於特定種子值）多次執行程式碼時可以產生相同的隨機數。
# 此功能對於測試程式碼很有幫助。例如，我們會隨機選擇一些資料來與機器學習演算法中的預測進行比較。我們將使用 seed() 函數使隨機選擇的資料保持一致。
random.seed(10)

for i in range(5):
    print(random.randint(1, 1000))
# 在所有主機都會輸出以下結果
# 在seed為10的情況下取5個隨機數，一定會是這5個並且順序相同
# 586
# 34
# 440
# 495
# 592


# 如果我們想從列表中隨機選擇元素或從字串中隨機選擇一個字符，那麼 Python 提供了簡單的函數可供使用。
# 1. random.choice(seq) : 從非空序列 seq 傳回一個隨機元素。如果 seq 為空，則引發 IndexError。
sentence = "Hi, I'm Joan"
print(random.choice(sentence))  # sentence中隨機一個字

# 2. random.choices(sequence, Weights=None, cum_weights=None, k=1) : 傳回從序列中選擇的 k 大小的元素清單並進行替換。如果序列為空，則引發 IndexError。
# Weights、cum_weights 和 k 都是可選的。我們可以從weights和cum_weights中選擇一個； cum_weights 被累積。
fruits = ["apple", "banana", "orange", "cherry"]
# weights總共是5，也就是說cherry被選到的機率是2/5其他都是1/5
# k=5就是會隨機選5個，可能會重複
print(
    random.choices(fruits, k=5, weights=[1, 1, 1, 2])
)  # ['banana', 'cherry', 'cherry', 'cherry', 'apple']

# 3. random.sample(sequence, k) : 傳回從總體序列或集合中選擇的 k 長度的"唯一"元素清單。用於無放回隨機抽樣(不會重複)。 k 不能為負數或大於序列的大小。
# 如果k大於sequence的長度則會出現ValueError: Sample larger than population or is negative
print(random.sample(fruits, k=3))  # ['cherry', 'banana', 'apple']

# 4. random.shuffle(x) : 將序列 x 打亂。序列 x 必須是可變的(tuple不可變)。由於是隨機的，所以有可能打亂後跟原本的一模一樣
# shuffle() 函數永久更改序列 x。

random.shuffle(fruits)
print(fruits)  # ['apple', 'cherry', 'orange', 'banana']

# 要打亂不可變序列並傳回新的打亂列表，請改用sample(x, k=len(x))。
my_tuple = (1, 4, 3, 6, 2, 7, 0)
print(random.sample(my_tuple, k=len(my_tuple)))  # [1, 6, 4, 3, 2, 7, 0]
print(my_tuple)  # (1, 4, 3, 6, 2, 7, 0)
# random.shuffle(my_tuple)
#     x[i], x[j] = x[j], x[i]
# TypeError: 'tuple' object does not support item assignment
