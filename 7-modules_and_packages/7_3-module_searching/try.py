# # 在python啟動時會創建一個sys.path，是一個list，其中的element是資料夾的路徑
# # 就是你使用module的時候python會去這些資料夾找有沒有要用的module
# import sys

# print(sys.path)
# ['c:\\Users\\22300711\\Desktop\\python_learning\\7-modules_and_packages\\7_3-module_searching', 'C:\\Users\\22300711\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\22300711\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\22300711\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\22300711\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\22300711\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages', "C:\\Users\\22300711\\Desktop\\python_learning\\'C:\\Users\\22300711\\whatever"]
# C:\\Users\\22300711\\whatever是我在C:\Users\22300711\AppData\Local\Programs\Python\Python39\Lib\site-packages
# 新增了sitecustomize.py內容為:
# import site
# site.addsitedir("'C:\\Users\\22300711\\whatever") # 在sys.path新增C:\\Users\\22300711\\whateve路徑
