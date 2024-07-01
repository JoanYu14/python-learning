# 1.r => read(預設)
with open("myFile.txt") as file:
    all_content = file.read()
    print(all_content)

# 2.a => append:新增內容到文件中
with open("myFile.txt","a") as appendFile:
    appendFile.write("\nIt's append content") # 新增這段字

# 3.w => write:寫入，會覆寫整個內容
with open("myFile2.txt","w") as writeFile:
    writeFile.write("It's write content") 

# 4.x => create:建立，建立一個檔案，若是已存在則出現錯誤
with open("myFile3.txt","x") as createFile:
    createFile.write("It's create content")
    # 若已存在:FileExistsError: [Errno 17] File exists: 'myFile2.txt'