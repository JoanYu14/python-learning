import os
# os.rmdir("not_empty_folder") # OSError: [WinError 145] 目錄不是空的。: 'not_empty_folder'
os.remove("want_delete_file.txt")
os.rmdir("want_delete_folder")