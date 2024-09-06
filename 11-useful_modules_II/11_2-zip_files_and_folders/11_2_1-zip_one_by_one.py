# zipfile模組是Python標準的zip檔模組；它支援無損資料壓縮。
# 無損壓縮是指壓縮演算法允許從壓縮資料完美地重建原始資料。
import zipfile
import os

# zipfile.ZipFile 是 Python 標準庫中 zipfile 模組的一個Class，用來處理 ZIP 文件的讀寫操作。這個類可以用來讀取、寫入或追加 ZIP 文件中的內容。
# class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True)
# file參數 : 這是需要讀取或寫入的 ZIP 文件，既可以是文件的路徑（字串），也可以是類似文件對象（如 BytesIO 等）。
# mode參數 : 用來指定打開 ZIP 文件的模式。默認值是 'r'（讀取模式）
# 'r'：只讀模式，讀取 ZIP 文件內容。
# 'w'：寫入模式，創建新的 ZIP 文件並將文件寫入其中。如果文件已存在，它將被覆蓋。
# 'a'：追加模式，將文件添加到現有的 ZIP 文件中。如果文件不存在，將創建一個新文件。
# 'x'：排他寫入模式，創建新的 ZIP 文件，如果文件已存在，則引發錯誤。

# compression參數 : 指定使用哪種壓縮算法。默認值是 zipfile.ZIP_STORED，表示不壓縮。可選值有：
# zipfile.ZIP_STORED：不壓縮。
# zipfile.ZIP_DEFLATED：使用 deflate 算法壓縮（這是最常用的壓縮方式）。
# zipfile.ZIP_BZIP2：使用 BZIP2 算法壓縮。
# zipfile.ZIP_LZMA：使用 LZMA 算法壓縮。

# allowZip64參數:默認為 True，這個參數允許處理大於 4GB 的 ZIP 文件。如果設為 False，則不允許處理超過這個限制的 ZIP 文件。
# compresslevel參數 : 用來控制壓縮等級，僅當 compression 為 ZIP_DEFLATED、ZIP_BZIP2 或 ZIP_LZMA 時有效。其值範圍通常是從 0 到 9，數值越高壓縮越密集，但會增加壓縮時間。
# strict_timestamps參數 : 默認為 True，確保在讀取或寫入 ZIP 文件時遵守嚴格的時間戳精度。如果設為 False，時間戳的精度將降低到兩秒，這是 ZIP 文件的一個舊特性。
want_zip_filepath1 = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "researchpaper1.txt",
)
want_zip_filepath2 = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "researchpaper2.txt",
)
zipped_filepath = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "researchpaper.zip",
)
zipped_file = zipfile.ZipFile(file=zipped_filepath, mode="w")

# arcname：此參數指定 ZIP 文件內的文件名，這樣可以避免保存完整的路徑。當你指定 arcname="researchpaper1.txt" 時，ZIP 文件內就只會有這個文件，而不會包含多餘的資料夾。
zipped_file.write(
    filename=want_zip_filepath1,
    compress_type=zipfile.ZIP_DEFLATED,
    arcname="researchpaper1.txt",
)
zipped_file.write(
    filename=want_zip_filepath2,
    compress_type=zipfile.ZIP_DEFLATED,
    arcname="researchpaper2.txt",
)
zipped_file.close()


# unzip解壓縮
unzip_path = os.path.join(
    os.getcwd(),
    "11-useful_modules_II",
    "11_2-zip_files_and_folders",
    "researchpaper_unzip_result",
)
zipped_obj = zipfile.ZipFile(file=zipped_filepath, mode="r")
# path參數為解壓所的檔案要放到哪個目錄(目錄不存在的話會自動創建)
zipped_obj.extractall(path=unzip_path)
zipped_obj.close()
