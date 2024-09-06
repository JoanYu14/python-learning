# zipfile模組不支援一次壓縮整個目錄。為此，我們需要
#     1. 使用 os.walk() 方法遍歷目錄中的每個子資料夾，並將所有內容壓縮在一起。 （不推薦）
#     2. 使用shutil模組內建方法shutil.make_archive()。 （受到歡迎的）
import os
import shutil

want_zip_folder = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "Employee",
)

output_path = os.path.join(
    os.getcwd(), "11-useful_modules_II", "11_2-zip_files_and_folders", "Employee_output"
)

# shutil.make_archive() 是 Python 標準庫中 shutil 模組提供的一個方便函數，用來創建壓縮檔案（如 ZIP、TAR 等格式）。
# 它可以打包一個整個目錄及其內容到壓縮文件中。
shutil.make_archive(base_name=output_path, format="zip", root_dir=want_zip_folder)


# 解壓縮
# shutil.unpack_archive() 是 Python 中 shutil 模組提供的函數，用來解壓縮不同格式的壓縮檔案（如 ZIP、TAR 等）到指定的目錄中。
want_unzip_file = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "Employee_output.zip",
)
unzipped_output_folder = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "shutil_unzip_employee_result",
)
shutil.unpack_archive(
    filename=want_unzip_file, extract_dir=unzipped_output_folder, format="zip"
)
