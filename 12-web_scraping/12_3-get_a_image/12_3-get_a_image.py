from bs4 import BeautifulSoup  # BeautifulSoup 是一個解析 HTML 的module
import lxml  # lxml 是 BeautifulSoup 支持的解析器之一
import os  # os 模組用於處理文件路徑
import requests  # requests 模組用於發送 HTTP 請求
import re  # re 模組用於正則表達式匹配

# 發送 HTTP GET 請求，獲取哈利波特維基百科頁面的 HTML 內容
result = requests.get(
    "https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9"
)

# 取得網頁的HTML內容
html_content = result.text

# 使用 BeautifulSoup 解析HTML內容，這裡選擇使用lxml解析器
soup = BeautifulSoup(html_content, "lxml")

# 正則表達式，用於匹配圖片的 src 屬性中包含 "platform" 或 "Platform" 的內容
platform_regex = r"platform|Platform"

# 使用 find 方法尋找第一個 img 標籤，其 src 屬性符合正則表達式 platform_regex
result = soup.find("img", {"src": re.compile(platform_regex)})

# 打印找到的 img 標籤
print(result)

# 打印 img 標籤的 src 屬性（圖片的 URL 路徑）
print(result["src"])

# 因為 src 可能不包含完整的 URL，需要加上 "https:" 來形成完整的圖片 URL
correct_url = f"https:{result['src']}"

# 使用 os.path.join 組合當前工作目錄和文件路徑，生成圖片的本地保存路徑
download_img_path = os.path.join(
    os.getcwd(), "12-web_scraping", "12_3-get_a_image", "harry_potter_platform.jpg"
)

# 發送 HTTP GET 請求，下載圖片的內容
img_result = requests.get(correct_url)

# 打開一個文件並以二進制模式寫入（因為圖片是二進位資料），將下載的圖片內容保存到本地
with open(download_img_path, "wb") as file:
    file.write(img_result.content)
