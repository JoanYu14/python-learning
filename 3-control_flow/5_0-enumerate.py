#enumerate() 函數會為可迭代物件新增一個計數器，並使它們成為一個包含 2 個元素的tuple。
# 計數器可讓您追蹤已發生的迭代次數。

for counter,word in enumerate("How are you today?"):
    #print(word) # (0, 'H') (1, 'e') ...
    if counter > 10:
        break
    else:
        print(word) # 只會print到y

for counter,number in enumerate(range(0,11,2)):
    # counter:0, value:0 counter:1, value:2 ... counter:5, value:10
    print(f'counter:{counter}, value:{number}') 