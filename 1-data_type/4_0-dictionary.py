# 字典方法示例
example = {"Joan":{"age":23,"friends":["Jessica","John","Jin"]},"Tim":"No Data"}
print(example["Joan"]) # {"age":23,"friends":["Jessica","John","Jin"]}
print(example["Joan"]["friends"][1]) # John
print(example["Tim"]) # No Data
example["James"] = {"age":39,"friends":["Wade","Anthony","Paul"],"job":"baseketball player"}
print(example["James"]["age"]) # 39


d = {'a': 1, 'b': 2, 'c': 3}
# 取字典key的value
print(d["b"]) #2

# keys()
print("keys:", d.keys())  # dict_keys(['a', 'b', 'c'])

# values()
print("values:", d.values())  # dict_values([1, 2, 3])

# items()
print("items:", d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# 將視圖轉換為列表
keys_list = list(d.keys())
values_list = list(d.values())
items_list = list(d.items())

print("keys list:", keys_list)  # ['a', 'b', 'c']
print("values list:", values_list)  # [1, 2, 3]
print("items list:", items_list)  # [('a', 1), ('b', 2), ('c', 3)]
