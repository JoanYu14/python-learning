# 在我們import random的時候其實Python去找到random.Random這個Class並使用該Class製作了一個instance，使用random.randint()…然後再使用這個instance的randint method
# 我們可以實例化自己的 Random 實例來取得不共享狀態的生成器。用random.Random Class的constactor來製作自己的object，就可以設定不同的seed，各自設定不同的seed就可以不用share state
import random

a = random.Random()
b = random.Random()
a.seed(10)
b.seed(15)
random.seed(5)
print(a.randrange(1, 100))  # 74
print(b.randrange(1, 100))  # 27
print(random.randrange(1, 100))  # 80
