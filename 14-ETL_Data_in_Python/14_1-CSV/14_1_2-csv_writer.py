# 要將資料寫入 CSV 文件，我們必須執行以下操作：
#     1. 使用 open() 函數以寫入模式或附加模式開啟 CSV 檔案。
#     2. 使用 Python csv.writer() 函數建立 writer 物件。
# 然後，我們可以使用：
#     writer.writerow(list) – 寫入一行資料。
#     writer.writerows(list of list) – 寫入幾行資料。

import csv  # 匯入 csv 模組，用於處理 CSV 格式的文件
import os  # 匯入 os 模組，用於處理文件路徑

# 使用 os.path.join 將當前工作目錄與子資料夾及文件名結合，生成完整的文件路徑
file_path = os.path.join(os.getcwd(), "14-ETL_Data_in_Python", "14_1-CSV", "new.csv")

# 使用 open 函數打開（或創建）指定的 CSV 文件
# mode="w" 表示以寫入模式開啟文件，這會創建新文件或清空已存在的文件
# newline="" 是為了避免在寫入 Windows 系統時自動添加多餘的空行
# encoding="utf8" 是指定 UTF-8 編碼來處理文件，避免因不同編碼而產生問題
with open(file_path, newline="", mode="w", encoding="utf8") as file:
    # 創建一個 csv.writer 實例，該實例會將資料寫入文件
    # delimiter="," 指定逗號為欄位分隔符
    csv_writer = csv.writer(file, delimiter=",")

    # 使用 writerow 方法寫入一行資料，這裡寫入的是表頭（column names）["a", "b", "c"]
    csv_writer.writerow(["a", "b", "c"])

    # 使用 writerows 方法批量寫入多行資料，這裡寫入了 [["e", "f", "g"], ["h", "i", "j"]]
    csv_writer.writerows([["e", "f", "g"], ["h", "i", "j"]])

# a,b,c
# e,f,g
# h,i,j
