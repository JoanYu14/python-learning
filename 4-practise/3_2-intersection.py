# 寫一個名為「intersection」的函數，它接受 2 個列表
# 並傳回位於 2 個列表交集的元素列表。
# intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]); # returns [3, 4]

def intersection(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set.intersection(set1,set2))

print(intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]))