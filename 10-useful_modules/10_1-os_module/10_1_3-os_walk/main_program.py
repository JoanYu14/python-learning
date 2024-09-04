# os.walk
# os.walk(path) 方法透過自上而下或自下而上遍歷樹來產生目錄樹中的檔案名稱。對於樹中以目錄頂部為根的每個目錄（包括頂部本身），它會產生一個 3 元組（目錄路徑(當前所在位置)、目錄名稱(當前目錄下還有哪些目錄)、檔案名稱(當前目錄底下有哪些檔案)）。
# os.walk(path) 方法使用深度優先樹遍歷演算法來決定列出目錄中資料夾、子資料夾和檔案資訊的順序。
import os


for i in os.walk(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "10_1_3-os_walk", "1")
):
    print(i)

# ('.\\10-useful_modules\\10_1-os_module\\10_1_3-os_walk\\1', ['2', '4'], ['in1.txt'])
# ('.\\10-useful_modules\\10_1-os_module\\10_1_3-os_walk\\1\\2', ['3'], ['in2.txt'])
# ('.\\10-useful_modules\\10_1-os_module\\10_1_3-os_walk\\1\\2\\3', [], ['in3.txt'])
# ('.\\10-useful_modules\\10_1-os_module\\10_1_3-os_walk\\1\\4', ['5'], ['in4.txt'])
# ('.\\10-useful_modules\\10_1-os_module\\10_1_3-os_walk\\1\\4\\5', [], ['in5.txt'])

for dirpath, dirnames, filenames in os.walk(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "10_1_3-os_walk", "1")
):
    print("========================================")
    print(f"當前路徑:{dirpath}")
    print("當前目錄下有以下目錄")
    # enumerate() 函數會為可迭代物件新增一個計數器，並使它們成為一個包含 2 個元素的tuple。
    for counter, dirname in enumerate(dirnames):
        print(f"目錄{counter+1}:{dirname}")
    print("當前目錄下有以下檔案")
    for counter, filename in enumerate(filenames):
        print(f"檔案{counter+1}:{filename}")
        # 使用splitext找出附檔名(tuple的第二項)，若為html檔就刪掉
        if os.path.splitext(os.path.join(dirpath, filename))[1] == ".html":
            print("是html檔")
# ========================================
# 當前路徑:.\10-useful_modules\10_1-os_module\10_1_3-os_walk\1
# 當前目錄下有以下目錄
# 目錄1:2
# 目錄2:4
# 當前目錄下有以下檔案
# 檔案1:in1.txt
# ========================================
# 當前路徑:.\10-useful_modules\10_1-os_module\10_1_3-os_walk\1\2
# 當前目錄下有以下目錄
# 目錄1:3
# 當前目錄下有以下檔案
# 檔案1:in2.txt
# ========================================
# 當前路徑:.\10-useful_modules\10_1-os_module\10_1_3-os_walk\1\2\3
# 當前目錄下有以下目錄
# 當前目錄下有以下檔案
# 檔案1:in3.txt
# ========================================
# 當前路徑:.\10-useful_modules\10_1-os_module\10_1_3-os_walk\1\4
# 當前目錄下有以下目錄
# 目錄1:5
# 當前目錄下有以下檔案
# 檔案1:in4.txt
# ========================================
# 當前路徑:.\10-useful_modules\10_1-os_module\10_1_3-os_walk\1\4\5
# 當前目錄下有以下目錄
# 當前目錄下有以下檔案
# 檔案1:in5.txt
