def addition(a,b):
    return a+b

def reduce(a,b):
    return a-b

print(f"reduce現在的記憶體位置為{reduce}") # reduce現在的記憶體位置為<function reduce at 0x000001D3FAE40550>
reduce = addition # reduce被指向到addition這個函數的位置了(copy by reference)
print(f"addition現在的記憶體位置變成{addition}") # addition現在的記憶體位置變成<function addition at 0x000001D3FAE404C0>
print(f"reduce現在的記憶體位置變成{reduce}") # reduce現在的記憶體位置變成<function addition at 0x000001D3FAE404C0>
print(reduce(4,5)) # 9

# str原本是build-in method，就是應保留字，但這邊被重新賦值了，雖然還是能賦值成功，但後續str()就不能使用了
str=3
print(str)
# print(str(123)) TypeError: 'int' object is not callable，str陰莖變成3了，不是函數了