# Beautiful Soup 是一個 Python 函式庫，用於從 HTML 和其他一些標記語言中取得資料。 Lxml 是一個用來解釋 HTML 的解析器。
# bs4 模組中的 BeautifulSoup(string, parser) 方法將一個字串和一個解析器作為輸入，並傳回一個特殊的 BeautifulSoup 物件。
# pip install bs4
# pip install lxml
import os
import re
from bs4 import BeautifulSoup


file_path = os.path.join(
    os.getcwd(), "12-web_scraping", "12_2-beautiful_soup_and_lxml", "file.html"
)
with open(file_path, "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "lxml")

print("============================= 1 ================================")
# 1. soup.find(name, attribute) - 傳回第一個符合的 TAG 物件。我們可以按名稱或屬性或兩者都進行搜尋。
soup_result1 = soup.find("a")
print(type(soup_result1))  # <class 'bs4.element.Tag'>
print(
    f"第一個a標籤為:{soup_result1}"
)  # 第一個a標籤為:<a class="sister" href="http://example.com/elsie" id="link1"> Elsie </a>

# 因為在python中class是保留字，所以beautiful soup中就用class_來代表class attribute
soup_result_class = soup.find(class_="title")
print(f"第一個class屬性帶有title的標籤為:{soup_result_class}")
# 第一個class帶有title的標籤為:<p class="title">
# <b> The Dormouse's story </b>
# </p>

# 找到a標籤中href attribute為http://example.com/lacie的element
soup_result2 = soup.find("a", href="http://example.com/lacie")
print(f"第一個a標籤中href attribute為http://example.com/lacie的element為{soup_result2}")
# 第一個a標籤中href attribute為http://example.com/lacie的element為<a class="sister" href="http://example.com/lacie" id="link2"> Lacie </a>

# =============================================================
print("============================= 2 ================================")
# 2. soup.find_all(name, attribute) - 傳回 TAG 物件List。
soup_result3 = soup.find_all("a")
print(
    f"soup_result3的type為{type(soup_result3)}"
)  # soup_result3的type為<class 'bs4.element.ResultSet'>
for counter, result in enumerate(soup_result3):
    print(f"第{counter+1}個a標籤為:{result}")
# 第1個a標籤為:<a class="sister" href="http://example.com/elsie" id="link1"> Elsie </a>
# 第2個a標籤為:<a class="sister" href="http://example.com/lacie" id="link2"> Lacie </a>
# 第3個a標籤為:<a class="sister" href="http://example.com/tillie" id="link3"> Tillie </a>
# 第4個a標籤為:<a class="sister" href="https://example.com/tillie" id="link4"> John </a>


# 篩選出以 "http://example.com/" 開頭的超鏈接，後面跟隨數字或非數字字符，直到遇到非雙引號的字符。
# 第4個a標籤是http"s"所以不會符合
regex1 = r'http://example.com/[\d|\D][^"]*'
# 這是一個屬性過濾器，指定要查找具有 href 屬性的超鏈接，且 href 的值要匹配之前定義的正則表達式 regex1。re.compile(regex1) 將正則表達式編譯為一個可被 find_all() 函數使用的正則表達式對象。
soup_result4 = soup.find_all("a", {"href": re.compile(regex1)})
for counter, result in enumerate(soup_result4):
    print(f"第{counter+1}符合regex1的a標籤為:{result}")
# 第1符合regex1的a標籤為:<a class="sister" href="http://example.com/elsie" id="link1"> Elsie </a>
# 第2符合regex1的a標籤為:<a class="sister" href="http://example.com/lacie" id="link2"> Lacie </a>
# 第3符合regex1的a標籤為:<a class="sister" href="http://example.com/tillie" id="link3"> Tillie </a>

# =============================================================

print("============================= 3 ================================")
# 3. tag.get(attributeName) - 傳回該標籤屬性中的值。
for counter, result in enumerate(soup_result3):
    print(f"第{counter+1}個a標籤的href屬性為:{result.get('href')}")
    print(
        f"result.get('href')的型別為{type(result.get('href'))}"
    )  # result.get('href')的型別為<class 'str'>
    print(f"第{counter+1}個a標籤的id屬性為:{result.get('id')}")
    print(f"第{counter+1}個a標籤的class屬性為:{result.get('class')}")
    print(
        f"result.get('class')的型別為{type(result.get('class'))}"
    )  # result.get('class')的型別為<class 'list'>
    # reulst.get('class')的型別為list的原因是一個tag可以有不只一個class

# 第1個a標籤的href屬性為:http://example.com/elsie
# 第1個a標籤的id屬性為:link1
# 第2個a標籤的href屬性為:http://example.com/lacie
# 第2個a標籤的id屬性為:link2
# 第3個a標籤的href屬性為:http://example.com/tillie
# 第3個a標籤的id屬性為:link3
# 第4個a標籤的href屬性為:https://example.com/tillie
# 第4個a標籤的id屬性為:link4

# 可以透過物件語法存取 TAG 物件的屬性。
# 例如，<p class=“hello my_P”> TAG物件儲存在變數h中，那麼我們可以執行print(h[“class”])，我們將得到[“hello”,“my_P”]。
print(f'soup_result2的id為{soup_result2["id"]}')  # soup_result2的id為link2
print(
    f'soup_result2的class為{soup_result2["class"]}'
)  # soup_result2的class為['sister']


# =============================================================

print("============================= 4 ================================")
# 4. tag.getText() - 傳回 HTML 標記的文字部分。
for counter, result in enumerate(soup_result3):
    print(f"第{counter+1}個a標籤的text為:{result.getText()}")
# 第1個a標籤的text為: Elsie
# 第2個a標籤的text為: Lacie
# 第3個a標籤的text為: Tillie
# 第4個a標籤的text為: John

# =============================================================

print("============================= 5 ================================")

# 在 CSS 中，有 CSS 選擇器語法來選擇特定的 HTML 元素，並對這些元素套用樣式。以下是一些規則：
# #someId – 將選擇 id=「someId」的所有 HTML 元素
# .someClass – 將選取所有 class=「someClass」 的 HTML 元素
# p.someClass – 將選擇所有帶有 class=“someClass”的 p 標籤

# 5. soup.select(CSSSelector) - 使用 CSS 選擇器語法傳回 TAG 物件清單。
css_soup_result1 = soup.select("#link4")
print(
    f"id屬性為link4的tag為{css_soup_result1}"
)  # id屬性為link4的tag為[<a class="sister" href="https://example.com/tillie" id="link4"> John </a>]
css_soup_reuslt2 = soup.select("p.story")
for counter, result in enumerate(css_soup_reuslt2):
    print(f"第{counter+1}個帶有sotry class的p標籤為:{result}")
    print()
# 第1個帶有sotry class的p標籤為:<p class="story">
#       Once upon a time there were three little sisters; and their names were
#       <a class="sister" href="http://example.com/elsie" id="link1"> Elsie </a>
#       ,
#       <a class="sister" href="http://example.com/lacie" id="link2"> Lacie </a>
#       and
#       <a class="sister" href="http://example.com/tillie" id="link3"> Tillie </a>
#       ; and they lived at the bottom of a well.
#       <a class="sister" href="https://example.com/tillie" id="link4"> John </a>
#       ; and they lived at the bottom of a well.
#     </p>
# 第2個帶有sotry class的p標籤為:<p class="story">...</p>
