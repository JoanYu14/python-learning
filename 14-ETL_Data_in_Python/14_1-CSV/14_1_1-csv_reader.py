# 當讀取csv檔案時，我們必須：
#     1. 使用 open() 函數開啟 CSV 檔案。
#     2. 使用 python 模組 functon csv.reader() 讀取 csv 檔案。借助csv reader，我們可以得到一個reader對象，並對該對象進行迭代。
import csv
import os

file_path = os.path.join(os.getcwd(), "14-ETL_Data_in_Python", "14_1-CSV", "file.csv")
# 當開啟 csv 檔案並使用 csv 模組讀取器和寫入器時，我們應該使用帶有 newline='' 的 open() 函數。
# 官方 csv 文件建議在所有平台上使用 newline='' 開啟文件，以停用通用換行符翻譯。
with open(file_path, newline="", mode="r", encoding="utf8") as file:
    csv_data = csv.reader(file)
    print(csv_data)  # <_csv.reader object at 0x000001738DACB880>
    for row in csv_data:
        print(row)
        print(row[1].title())  # 會把每個單字的第一個字元變成大寫
# ['id', 'name', 'year of birth']
# Name
# ['1', 'albert einstein', '1879']
# Albert Einstein
# ['2', 'isaac newton', '1643']
# Isaac Newton
# ['3', 'marie curie', '1867']
# Marie Curie
# ['4', 'galilée', '1564']
# Galilée
