import os
import re

data_dir_path = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_1-Regular_Expression",
    "11_1_4-Regular_Expression_practise",
    "11_1_4_2-fine_employee_number",
    "Employee",
)

regex1 = r"\d{3}-\d{3}-\d{4}"
answer = []
# os.walk(path) 方法透過自上而下或自下而上遍歷樹來產生目錄樹中的檔案名稱。對於樹中以目錄頂部為根的每個目錄（包括頂部本身），它會產生一個 3 元組（目錄路徑(當前所在位置)、目錄名稱(當前目錄下還有哪些目錄)、檔案名稱(當前目錄底下有哪些檔案)）。
for dirpath, dirnames, filenames in os.walk(data_dir_path):
    if filenames:
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            answer.extend(re.findall(regex1, content))

for counter, number in enumerate(answer):
    print(f"號碼{counter+1}: {number}")

# 號碼1: 741-776-5632
# 號碼2: 874-965-7544
# 號碼3: 969-741-6350
# 號碼4: 808-765-3211
# 號碼5: 754-658-9650
# 號碼6: 740-665-7400
# 號碼7: 740-850-9666
# 號碼8: 785-968-8500
# 號碼9: 888-741-6360
