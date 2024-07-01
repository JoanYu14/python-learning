# 寫一個名為「position」的函數，傳回第一個大寫字母及其索引位置的元組。如果沒有找到，則傳回-1。
def position(words):
    for counter,word in enumerate(words):
        if(word and word==word.upper()):
            return (word,counter)
    return -1

words = input("請輸入字串:").replace(" ","")
print(position(words))