# 1. file = open(filename) - 開啟檔案並將其作為檔案物件傳回。
file = open("myFile.txt") # 若是要這樣寫的話，請確保終端機目前位置為當前directory
print(file) # <_io.TextIOWrapper name='myFile.txt' mode='r' encoding='cp950'>
file.close()

# 2. file.read() – 從檔案中傳回指定的位元組數。
file = open("myFile.txt")
print(file.read(6)) #  My nam
print(file.tell()) # 6 => 這是retrun當前文件指針的位置
print(file.read()) # 從第6個字往後的所有字
print(file.tell()) # 55 => 文件最後面的位置
file.seek(0) # 將文件指針移回起點
print(file.tell()) # 0
file.close()
# 因為前面用了file.read(6)，所以再用file.read的話會從第6個字開始
# 文件指針（file pointer）會移動到已讀取的字元之後，即從第7個字元開始。
# 這樣，當你後續再次調用 file.read() 時，它會從文件指針當前位置繼續讀取，而不是從文件的開頭開始。
# e is Joan
# I'm 23 years old
# I come from Pingtung

# 3. file.readline() – 傳回目前位置的一行文字。
# 通常用這個是當不知道file的內容有多大的話，就用這個函數來一行行讀，這樣就可以避免記憶體被塞滿
file = open("myFile.txt") 
print("file.readline())")
print(file.readline()) # My name is Joan
while True:
    line = file.readline()
    if not line: # 空字串為folsy value
        break
    else:
        print(line)
file.close()

# 4. file.readlines() – 傳回一個列表，其中包含檔案中的每一行作為列表項目。
file = open("myFile.txt") 
print("file.readlines()")
print(file.readlines()) # ['My name is Joan\n', "I'm 23 years old\n", 'I come from Pingtung']
file.close()

# 5. file.seek(offset) 是一個用於在文件操作中移動文件指針的方法。這個方法可以讓你控制從文件的特定位置開始讀取或寫入數據。
# 從文件開頭移動到指定位置：
file = open("myFile.txt", "r")
file.seek(10)  # 將文件指針移動到文件的第11個字節（假設以字節為單位）
data = file.read()  # 從這個位置開始讀取文件數據
print(data)
file.close()

# 以下whence=1 or =2 Python 的文件物件（TextIOWrapper）不支持使用，只能用whence=0相對起始絕對位置
# # 相對於當前位置向前移動或向後移動：
# file = open("myFile.txt","w")
# file.seek(20, 1)  # 相對於當前文件指針位置向後移動20個字節
# data = file.read()  # 從這個新位置開始讀取文件數據
# print(data)
# file.close()

# # 從文件末尾向前移動：
# file = open("myFile.txt", "r")
# file.seek(-10, 2)  # 相對於文件末尾向前移動10個字節
# data = file.read()  # 從這個新位置開始讀取文件數據
# print(data)
# file.close()

