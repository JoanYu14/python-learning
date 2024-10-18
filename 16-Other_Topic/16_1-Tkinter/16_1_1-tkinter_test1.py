# Tkinter 位於 Python 標準函式庫中，用於建立圖形使用者介面 (GUI)，並包含在所有標準 Python 發行版中。
# 我們可以使用Tkinter來製作桌面應用程式。

from tkinter import *  # 匯入 Tkinter 庫中的所有函數與類別

root = Tk()  # 建立主視窗 (root)，它是整個應用程式的容器

# 建立一個 Label (標籤) 物件，將其放入 root 視窗，並設定顯示的文字為 "This is my text"
myLabel = Label(root, text="This is my text")

myLabel.pack()  # 使用 pack() 方法將 Label 安排到主視窗中，自動處理佈局

root.mainloop()  # 啟動主視窗的事件循環，讓應用程式持續運行直到視窗被關閉
