# Counter(計數器)
# Counter 是一個 dict 子類，用來計算可哈希物件的數量。 （這就是第一個字母 C 大寫的原因。）它是一個集合，其中元素儲存為字典鍵，它們的計數儲存為字典值。
from collections import Counter

my_list = [1, 2, 2, 1, 3, 3, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 2]
# 建立一個新的空 Counter 物件。如果給定，則計算元素數
# 參數為一個iterable物件。或者，從另一個映射初始化計數元素的數量。
result = Counter(my_list)
print(result)  # Counter({2: 10, 1: 5, 3: 2, 4: 1})

# dict.items()會將字典的key與value製作成一個個tuple組成的list
# 由於Counter是dict的子類，所以繼承dict的所有method
for key, value in result.items():
    print(f"{key}出現{value}次")

# most_common
# 函數most_common()是python內建模區塊collections中的Counter Class的函數
# most_common() 方法返回一個列表，其中包含計數器中出現頻率最高的元素及其出現次數。這些元素按照出現頻率的降序排列。
print(result.most_common())
# 找出出現頻率最高的1個字符
print(result.most_common(1))  # [(2, 10)]
# 找出出現頻率最高的3個字符
print(result.most_common(3))  # [(2, 10), (1, 5), (3, 2)]


class Mycounter:
    def __init__(self, data):
        # 檢查傳入的參數是否是可迭代對象（即是否具有 __iter__ 方法）
        if "__iter__" not in dir(data):
            # 如果傳入的參數不是可迭代對象，則拋出 TypeError 異常
            raise TypeError("參數必須是iterable的")

        # 初始化方法，接收一個可迭代對象（例如列表或字符串），並將其存儲在 self.data 中
        self.data = data

    @property
    def counter(self):
        # counter 屬性方法，計算 self.data 中每個元素的出現次數並返回一個字典
        dic = dict()  # 初始化一個空字典，用來存儲元素的計數
        for i in self.data:  # 遍歷 self.data 中的每個元素
            if i not in dic:  # 如果元素 i 不在字典中，則新增鍵值對，計數設為 1
                dic[i] = 1
            else:
                dic[i] += 1  # 如果元素 i 已經在字典中，則將其計數加 1
        return dic  # 返回計數結果的字典

    def most_common(self, num=None):
        # most_common 方法，返回最常見的元素及其計數
        counter = self.counter  # 獲取 counter 字典，該字典包含每個元素的計數
        items = counter.items()  # 將字典轉換為 (鍵, 值) 的元組列表
        print(f"items:{items}")  # items:dict_items([(1, 5), (2, 10), (3, 2), (4, 1)])
        # 按照計數從高到低對 items 進行排序
        # key=lambda point: point[1] 指定了排序的鍵值（key）。
        # 這裡的 Lambda 函式 lambda point: point[1] 接受一個參數 point(這裡傳入items)，並返回 point 元組的第二個元素（即 point[1]），這樣就根據每個元組的第二個元素來進行排序。
        sorted_counter = sorted(items, key=lambda point: point[1], reverse=True)

        if num:
            # 如果提供了 num 參數，返回前 num 個最常見的元素
            return sorted_counter[0:num]
        else:
            # 如果未提供 num 參數，返回所有元素及其計數，按降序排列
            return sorted_counter


mycounter = Mycounter([1, 2, 2, 1, 3, 3, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 2])
print(
    f"mycounter的counter屬性值為:{mycounter.counter}"
)  # mycounter的counter屬性值為:{1: 5, 2: 10, 3: 2, 4: 1}
print(mycounter.most_common(3))  # [(2, 10), (1, 5), (3, 2)]

try:
    error_counter = Mycounter(1)
except Exception as error:
    print(error)  # 參數必須是iterable的
