import requests

parameters = {"key1": 1, "key2": 2}
# https://www.example.com是一個用於示範和測試的網站，通常在教學資料和技術文檔中被使用。它並不是一個真正提供內容的網站，而是一個占位符，用於展示如何構建和使用 URL。這個網站是由 IANA（Internet Assigned Numbers Authority）管理的，主要目的是為了提供一個可以安全使用的示例網址。
# params為設定get請求要帶的參數
result = requests.get("https://www.example.com", params=parameters)
print(result)  # <Response [200]>
print(type(result))  # <class 'requests.models.Response'>
print(result.url)  # https://www.example.com/?key1=1&key2=2
print(f"Response的status code為{result.status_code}")  # Response的status code為200
print(result.encoding)  # UTF-8
print(result.headers)
# {'Content-Encoding': 'gzip', 'Age': '52733', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Fri, 06 Sep 2024 09:21:25 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Fri, 13 Sep 2024 09:21:25 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECAcc (lac/55A1)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '648'}
print(type(result.text))  # <class 'str'>
print("------------------")
print(result.text)  # html原始碼
