# argv 是 sys 模組中的一個列表（list），用來存儲命令行參數（Command Line Arguments），即在執行 Python 程式時從命令行傳入的參數。
# 在命令行執行 python example.py arg1 arg2 時，argv 就會包含 ['example.py', 'arg1', 'arg2']
from sys import argv
import os
if (len(argv)<2):
    print("請給文件名")
else:
    file = open(f'{os.path.dirname(__file__)}\\{argv[1]}')
    lines = file.read()
    lines = lines.split("\n")
    words = 0
    letters = 0
    for i in lines:
        words += len(i.split(" "))
        letters += len(i)
    print(f'有{len(lines)}行，{words}個單字，{letters}個字')