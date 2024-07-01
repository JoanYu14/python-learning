# hash function雜湊函數
# hash()是一種將一個值轉換為另一個值的函數。在Python中，雜湊函數基本上會傳回一個固定大小的整數。
# 可雜湊 : 整數integer、浮點數float、字串string、布林值boolean、元組tuple和 None。元組tuple中的所有元素element都需要是可雜湊的
# 不可雜湊 : 集合set、列表list、字典dictionary

a = hash(234)
a_string = hash("234")
b = hash(234.0)
b_string = hash("234.0")
c = hash("hello world")
d = hash(True)
# e = hash(([1,2,{2,3},{"key":"value"}],1,"2"))
e = hash((234,234.0,"hello world",True,None))
f = hash(None)


print(f"a為{a}") # a為234
print(f"a_string為{a_string}") # a_string為-1155939783937515596
print(f"b為{b}") # b為234
print(f"b_string為{b_string}") # b_string為6517299125436907978
print(f"c為{c}") # c為-1906687619579702879
print(f"d為{d}") # d為1
print(f"e為{e}") # e為8176233225605450684
print(f"e的type為{type(e)}") # e的type為<class 'int'>
print(f"f為{f}") # f為-9223363241128242483
# 可以發現把string拿去hash較有意義