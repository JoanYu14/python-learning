import sys


def main():
    # 從標準輸入讀取所有內容（例如 infile.txt 的內容）
    contents = sys.stdin.read()

    # 用 sys.argv[2] 取代 contents 中的所有 sys.argv[1]
    new_contents = contents.replace(sys.argv[1], sys.argv[2])

    # 將替換後的內容寫入標準輸出（例如 outfile.txt）
    sys.stdout.write(new_contents)


# 呼叫 main 函數，開始執行程序
main()
