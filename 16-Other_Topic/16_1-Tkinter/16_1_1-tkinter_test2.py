import tkinter as tk  # 匯入 Tkinter 並命名為 tk，這樣我們可以透過 tk 來使用它的功能

root = tk.Tk()  # 建立主視窗 (root)

# 建立一個 Canvas (畫布) 物件，設定寬度和高度為 300x300，並將其添加到 root 視窗
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()  # 使用 pack() 方法將 Canvas 放置到視窗中


# 定義一個函數，當按鈕被點擊時執行
def hello():
    # 建立一個 Label (標籤)，顯示 "Hello World!"，字體顏色 (foreground color) 設定為綠色，
    # 並將字體設定為 helvetica，字體大小為 12，字體樣式為粗體 (bold)
    label = tk.Label(
        root, text="Hello World!", fg="green", font=("helvetica", 12, "bold")
    )

    # 在 Canvas 的指定位置 (150, 200) 建立一個包含 label 的窗口
    canvas.create_window(150, 200, window=label)


# 建立一個 Button (按鈕)，當按鈕被點擊時，會觸發 hello 函數，按鈕顏色設定為黑色
button = tk.Button(text="Click me!!", fg="black", command=hello)

# 在 Canvas 的指定位置 (150, 150) 建立一個包含 button 的窗口
canvas.create_window(150, 150, window=button)

root.mainloop()  # 啟動主視窗的事件循環，讓應用程式持續運行直到視窗被關閉
