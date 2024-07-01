# 字串的index
print("hello"[0]) # h
print("hello"[-1]) # o
print("hello"[-5]) # h，因為倒著的話index是由-1開始(倒數第一個)而不是-0
#print("hello"[5]) # IndexError: string index out of range
#print("hello"[-6]) # IndexError: string index out of range

# 字串的slicing(切片)
# stringValue[開始index:結束index(但不包含):每次移動幾個index(可不填)]
print("hello[1:4]=>","hello"[1:4]) # eLL 
print("hello[1:1]=>","hello"[1:1]) # hello[1:1]=> 空
print("hello[1:6:3]=>","hello"[1:6:3]) # eo，從1開始到6(不包含6)，每次移動3，顯示index1與index4的字
print("hello[3:0:-1]=>","hello"[3:0:-1]) # lle，從3開始到0(不包含0)，每次移動-1(向左移動1)
print("hello[::-1]=>","hello"[::-1]) # olleh，倒著顯示
print("hello[1:1]=>","hello"[::1])  # hello

# 單引號雙引號
print('I say "hello"') 

# string是不可變的，不能從字串中取出個別字做賦值
#word = "Hello"
#word[0] = "h"  TypeError: 'str' object does not support item assignment


