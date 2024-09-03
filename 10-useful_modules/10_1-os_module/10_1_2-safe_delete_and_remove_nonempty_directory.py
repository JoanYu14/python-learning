import os

# 可以將檔案丟到垃圾桶的module，需要使用pip install send2trash
import send2trash

# shutil(shell utility) module，提供了一系列高階操作檔案與資料夾的方法，可以針對檔案進行複製、移動、壓縮、解壓縮等相關操作，
# 我們使用此模組來刪除不為空的目錄
import shutil

send2trash.send2trash(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "send2trash_test.txt"),
)

# shutil.rmtree()會以遞迴的方式刪除資料夾下的所有子資料夾和子檔案。
shutil.rmtree(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "nonempty_dir"),
)
