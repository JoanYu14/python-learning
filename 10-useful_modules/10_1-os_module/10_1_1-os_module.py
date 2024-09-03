import os

# ===== Command Fcuntions in OS Module =====

# 傳回表示目前工作目錄的字串。
print(os.getcwd())  # C:\Users\22300711\Desktop\python_learning(當前working directory)

# 傳回一個列表，其中包含路徑給定目錄中的條目名稱。請注意，os.listdir() 的預設參數是一個點。在 Windows 和 Linux/UNIX 中，點代表目前目錄。
print(os.listdir(path="."))
# ['.git', '1-data_type', '10-useful_modules', '2-operators_truthy_and_falsy_values', '3-control_flow', '4-funcions_and_method', '4-practise', '5-io_in_python', '6-object_oriented_programming', '7-modules_and_packages', '8-error_handling_and_exceptions', '9-advanced_functions']

# 是表示目前目錄的常數。例如，它是“.”在 Linux、Windows 和 OS X 上。然而，在舊的 Mac OS 9 系統上則為「:」。
print(os.curdir)  # .

# 是代表父目錄的常數。
print(os.pardir)  # ..

# ===== os.path =====

# os.path.join(path1, path2):智慧地連接一個或多個路徑元件。
# . ..是以working directory(當前終端機位置)為基準，而不是該py檔為基準
print(os.path.join(".", "9-advanced_functions"))  # .\1-data_type
print(
    os.listdir(os.path.join(".", "9-advanced_functions"))
)  # ['9_1-Decorators.py', '9_2-Generator.py', '9_3-Iteration_Iterable_Iterator.py', '9_4-Stdin_Stdout_and_Pipe']

# os.path.split(path) - 將基本名稱和目錄名稱分割為一個tuple元組。
print(os.path.split(os.getcwd()))  # ('C:\\Users\\22300711\\Desktop', 'python_learning')

# os.path.basename(path) – 傳回給定路徑的basename。
print(os.path.basename(os.getcwd()))  # python_learning

# os.path.dirname(path) – 傳回給定路徑的路徑的directory name。
print(os.path.dirname(os.getcwd()))  # C:\Users\22300711\Desktop

# os.path.splitext(path) – 傳回一個將檔案類型與路徑分開的元組。
print(os.path.splitext(os.path.join(".", "9-advanced_functions", "9_1-Decorators.py")))
# ('.\\9-advanced_functions\\9_1-Decorators', '.py')


# os.path.abspath(path) – 傳回給定路徑的絕對路徑。
print(os.path.abspath(os.path.join(".", "9-advanced_functions", "9_1-Decorators.py")))
# C:\Users\22300711\Desktop\python_learning\9-advanced_functions\9_1-Decorators.py

# ===== Other os.path methods =====

# os.path.isfile(path) – 傳回一個布林值，指示路徑是否為一個檔案。
print(
    os.path.isfile(
        os.path.abspath(os.path.join(".", "9-advanced_functions", "9_1-Decorators.py"))
    )
)  # True

# os.path.isdir(path) – 傳回一個布林值，指示路徑是否為目錄。
print(
    os.path.isdir(os.path.join(".", "9-advanced_functions", "9_1-Decorators.py"))
)  # False
# os.path.exists(path) – 傳回一個布林值，指示路徑（檔案或目錄）是否存在。
print(
    os.path.exists(os.path.join(".", "9-advanced_functions", "9_1-Decorators.py"))
)  # True

# ===== Other os module function =====

# os.name是一個常數，供我們檢查目前作業系統。
print(os.name)  # nt (new technology)

# os.rename(oldpath, newpath) – 將舊檔案名稱變更為新檔案名稱。
os.rename(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "test.txt"),
    os.path.join(".", "10-useful_modules", "10_1-os_module", "test1.txt"),
)  # 已改名後又在執行一次會出現FileNotFoundError: [WinError 2] 系統找不到指定的檔案。

# os.remove(filepath) – 刪除給定路徑的檔案。 （這是不可逆的！該檔案不會移至垃圾箱。相反，它會被永久刪除。）
os.remove(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "test1.txt"),
)
# os.rmdir(directorypath) – 如果給定目錄的路徑為空，則永久刪除目錄。若目錄中還有檔案的話就會出現OSError: [WinError 145] 目錄不是空的。
os.rmdir(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "empty_dir"),
)
# os.mkdir(name) – 建立一個新目錄。
os.mkdir(
    os.path.join(".", "10-useful_modules", "10_1-os_module", "new_empty_dir"),
)
