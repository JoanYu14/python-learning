# 編寫一個名為「swap」的函數
# 該函數接受一個字串作為輸入，並傳回一個小寫變為大寫、大寫變為小寫的新字串。
def swap(string):
    # 生成器
    # 解析生成器表達式的運作方式：
    # - 對於字串 string 中的每個字元 x，如果 x 是小寫則轉換為大寫，否則轉換為小寫。
    string_generator = (x.upper() if x==x.lower() else x.lower() for x in string)
    new_string = ""
    for i in string_generator:
        new_string+=i
    return new_string

input_string  = input("請輸入字串:")
print(f"新的字串為:{swap(input_string)}")