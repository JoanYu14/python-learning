# 我們也可以從 csv 檔案讀取數據，然後將其寫入新的 excel 檔案：
#     1. 建立一個 Excel 工作簿，就是建立一個新的excel檔案。
#     2. 工作簿始終至少包含一個工作表(在我們打開一個workbook的時候就有預設一個workbook正在使用的worksheet)。
#        我們可以透過使用 Workbook.active 屬性來取得它。
#     3. 設定工作表的標題。
#     4. 將每個資料行附加到工作表中。
#     5. 儲存工作簿。
from openpyxl import Workbook  # 匯入 openpyxl 的 Workbook 類，用於創建和操作 Excel 檔案
import csv  # 匯入 Python 內建的 csv 模組，用於讀寫 CSV 檔案
import os  # 匯入 os 模組，用來操作文件路徑

csv_file_path = os.path.join(
    os.getcwd(), "14-ETL_Data_in_Python", "14_1-CSV", "file.csv"
)

# 使用 csv.reader 讀取 CSV 檔案，將其內容轉換為列表
data_rows = [
    fields  # fields 是 CSV 檔案中的一行資料，解析後為列表形式
    for fields in csv.reader(open(csv_file_path, newline="", mode="r", encoding="utf8"))
]
# 結果將是一個包含每一行資料的列表，例如：[['id', 'name', 'year of birth'], ['1', 'albert einstein', '1879'], ...]

print(data_rows)  # 輸出 CSV 資料，檢查是否正確讀取

# 創建一個新的 Workbook 對象，這是用來處理 Excel 文件的
wb = Workbook()
# 獲取當前活躍的工作表（預設創建時，會有一個活躍的空白工作表）
ws = wb.active
# 將該工作表的名稱設為 "MyFile"
ws.title = "MyFile"

# 遍歷 data_rows，並將每一行資料添加到 Excel 工作表中
for row in data_rows:
    ws.append(row)  # 將 row 列表插入到工作表的行中，append 方法自動按行添加資料

# 指定保存 Excel 檔案的路徑
excel_file_path = os.path.join(
    os.getcwd(), "14-ETL_Data_in_Python", "14_2-Excel", "new_file.xlsx"
)

# 設定工作表標籤的顏色，這裡使用十六進制顏色碼 "1072BA"（藍色）
ws.sheet_properties.tabColor = "1072BA"

# 將工作簿保存到指定的 excel_file_path 中
wb.save(excel_file_path)
