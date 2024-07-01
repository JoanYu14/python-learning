# 集合方法示例

# difference()
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("difference:", s1.difference(s2))  # {1, 2}

# intersection()
print("intersection:", s1.intersection(s2))  # {3, 4}

# isdisjoint()
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print("isdisjoint:", s1.isdisjoint(s2))  # True

s3 = {3, 4, 5}
print("isdisjoint:", s1.isdisjoint(s3))  # False

# issubset()
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print("issubset:", s1.issubset(s2))  # True

s3 = {2, 3, 4}
print("issubset:", s1.issubset(s3))  # False

# issuperset()
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print("issuperset:", s1.issuperset(s2))  # True

s3 = {2, 3, 6}
print("issuperset:", s1.issuperset(s3))  # False

# union()
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
print("union:", s1.union(s2, s3))  # {1, 2, 3, 4, 5, 6, 7}
