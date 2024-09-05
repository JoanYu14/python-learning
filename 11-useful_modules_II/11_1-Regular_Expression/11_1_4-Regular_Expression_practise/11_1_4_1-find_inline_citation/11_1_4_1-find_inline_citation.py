# 1. inline-citation
# (alphanumeric or space , number >= 4)
import os
import sys
import re

file_path = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_1-Regular_Expression",
    "11_1_4-Regular_Expression_practise",
    "11_1_4_1-find_inline_citation",
    "researchpaper.txt",
)

# 讀取file_path的內容，編碼為utf-8
with open(file_path, "r", encoding="utf-8") as file:
    all_content = file.read()  # 將內容存到all_content


# \[(\]：匹配左括號 (
# ([1-9a-zA-Z\s]+)：第一組捕獲括號，匹配字母,數字或空格
# , : 匹配逗號,
# (\s{1}\d{4,})：第二組捕獲括號，匹配逗號、空格和至少 4 個數字
# \[)\]：匹配右括號 )
regex1 = r"[(]([1-9a-zA-Z\s]+),(\s{1}\d{4,})[)]"
# regex1 = r"[(]\w+|\s,\s\d{4,}[)]"
result1 = re.findall(regex1, all_content)
for counter, (name, year) in enumerate(result1):
    print(f"inline-citation{counter+1} - 名稱:{name} 年份:{year}")
# inline-citation1 - 名稱:Green Mountain Energy 年份: 2017
# inline-citation2 - 名稱:Mearns 年份: 2014
# inline-citation3 - 名稱:Lower 年份: 2018
# inline-citation4 - 名稱:Choi 年份: 2008
# inline-citation5 - 名稱:KHON2 News 年份: 2012
# inline-citation6 - 名稱:Campbell 年份: 2014
