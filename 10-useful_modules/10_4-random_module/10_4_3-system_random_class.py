# random預設使用random.Random Class，這個class使用Mersenne Twister PRNG演算法。
# 這個演算法在加密上並不安全；這是因為觀察足夠數量的迭代（在 MT19937 的情況下為 624 次，因為這是產生未來迭代的狀態向量的大小）在624次後就可以預測所有未來的迭代。

# SystemRandom 在 POSIX 系統上使用 /dev/urandom 文件，在 Windows NT 系統上使用 CryptGenRandom() 函數。兩者都是加密安全的 PRNG。 （稱為 CSPRNG）
# 我們之所以涉及操作系統，是因為隨機數字來自操作系統，操作系統有一個特殊的驅動程序，可以從各種現實世界的來源收集熵，例如擊鍵和磁碟尋道之間的時間變化。
# 我們能否準確預測下一次按鍵的時間，或者哪個鍵，或者下一次磁碟尋道何時發生，或者需要多長時間 - 所有這些本質上都是不可預測的（即使對機器進行物理訪問），所以它們可用於產生隨機數。


import random

a = random.Random()
b = random.SystemRandom()
print(a.randint(10, 100))
print(b.randint(10, 100))
