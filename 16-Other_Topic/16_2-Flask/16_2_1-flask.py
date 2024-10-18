# Flask 是 Python 中的一個 Web 框架，可讓我們輕鬆開發 Web 應用程式。它還包括 URL 路由和模板引擎(template engine)等功能。
from flask import Flask, jsonify, render_template

# create flask app
app = Flask(__name__)


# 首頁
# @app.route("/")
# def index():
#     return "This is my homepage!"


# 到/或/hello都會執行home function
# /hello/後面的東西會被當做執行home function的name參數的值
# 定義一個路由 ("/") 和另一個可選的動態路由 ("/hello/<name>")
# 這裡 "<name>" 是一個 URL 參數，會傳遞給函數作為參數
@app.route("/")  # 根路徑
@app.route("/hello/<name>")  # 動態路徑，根據 URL 傳入的 name 顯示
def home(name=None):  # 如果沒有提供 name，name 會是 None
    # 將 HTML 範本 index.html 渲染並回傳給使用者，並將 name 變數傳遞給模板
    # index.html 是一個範本檔案，會根據 name 動態顯示內容
    return render_template("index.html", name=name)


# 定義另一個路由 ("/info")，只接受 POST 請求
@app.route("/info", methods=["POST"])
def info():
    # 回傳一個 JSON 格式的訊息作為回應，表示請求成功
    return jsonify({"info": "You have successfully made a request."})


# 主程式進入點，檢查當前的模組名稱是否是 "__main__"
# 如果是，表示程式是直接被執行，而非作為模組被匯入，因此啟動 Flask 應用程式
if __name__ == "__main__":
    # 啟動應用程式，debug 模式會讓開發者能夠在程式出錯時看到更詳細的錯誤訊息
    app.run(debug=True)
