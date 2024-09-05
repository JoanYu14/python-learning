# Regular Expression正規表示式（又稱 regex）是指定文字中搜尋模式的字元序列。
# 正規表示式的概念始於 20 世紀 50 年代，當時美國數學家 Stephen Cole Kleene 形式化了正規語言的描述。
# 正規表示式使我們能夠搜尋文字資料中的一般模式；例如，一個簡單的電子郵件格式可以是 user@email.com，我們知道我們正在尋找一個模式“whatever”+@+“whatever”+“.com”

import re  # import Regular Expression Module

text = "from, my phone number is 0912345678. I am available from 10am to 5pm. fromit"
patt1 = "from"
patt2 = "from1"

# re.search只會找到第一個符合的
print(re.search(patt1, text))  # <re.Match object; span=(46, 50), match='from'>
print(re.search(patt2, text))  # None
match_result = re.search(patt1, text)
print(match_result.group())  # from
print(match_result.span())  # (0, 4)
print(match_result.start())  # 0
print(match_result.end())  # 4

# re.findall()
all_match_result = re.findall(patt1, text)
print(all_match_result)  # ['from', 'from', 'from']
