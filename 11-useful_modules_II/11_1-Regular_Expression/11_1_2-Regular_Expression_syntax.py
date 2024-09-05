import re

# print(r"") => raw string
# 在raw string裡面的任何字串都是字串而已沒有其他意義，例如\n不會是換行
# 在用regular expression用raw string較好，能避免Special String Characters
print(r"\n")  # \n

# Regular Expression Syntax 正規表示式語法
# 1. 語法【[]】
#    描述 : 用於表示一組字元。它可以被認為是一個定制的點。集合中的 – 表示從...到...。對於00到59之間的任何數字，我們可以做r“[0-5][0-9]”。就是第一個字只能介於0~5，第二個字只能介於0~9，對於任何英文字母，我們可以做r”[a-zA-Z]”
#    正規表示式 : r"he[abcl][a-d]o"
#    意思 : index0~1要是he，index為2的字只能是a,b,c,l其中一個，index為3的字只能介於a~d(a,b,c,d)，index4要是o
#    匹配 : “heaao”, “hecco”
text1 = r"hello, heaao, hecco, hexao"
print("----- syntax1 -----")
print(re.findall(r"he[abcl][a-d]o", text1))  # ['heaao', 'hecco']

# 2. 語法【.】
#    描述 : 點匹配除換行符之外的任何字元
#    正規表示式 : r”he..o”
#    意思 : index0~1要是he，index4要是o，index2,3是甚麼都可以
#    匹配 : “hello”, “hek5o”
print("----- syntax2 -----")
text2 = r"hello, heaao, hecco, hexao, hellooooo, helllo"
print(re.findall(r"he..o", text2))  # ['hello', 'heaao', 'hecco', 'hexao', 'hello']


# 3. 語法【*】
#    描述 : 克萊恩星。它匹配某事物出現 0 次或多次。它適用於任何字母數字字元、\、點和 []。
#    正規表示式 : r”ab*”
#    意思: index0必須是a，index1可以是1個b，多個b，0個b
#    匹配 : “a”, “ab”, “abbbbb”
print("----- syntax3 -----")
text3 = r"a, ab ,abbbbb, ac, abc, abbbbc, acc, abdc"
print(re.findall(r"ab*", text3))  # ['a', 'ab', 'abbbbb', 'a', 'ab', 'abbbb']
print(
    re.findall(r"ab*c", text3)
)  # ['ac', 'abc', 'abbbbc', 'ac'] => index0必須是a，最後一個index必須是c，中間的index必須是b或沒有b(不能是除了b以外的)
print(re.findall(r"[a-c]*", text3))
# a', '', '', 'ab', '', '', 'abbbbb', '', '', 'ac', '', '', 'abc', '', '', 'abbbbc', '', '', 'acc', '', '', 'ab', '', 'c', '']
text3_1 = r"hello, heaao, hecco, hexao"
# index0,1必須是he，最後一個index必須是o，中間有任何數量的任何其他字都沒關係
print(re.findall(r"he.*o", text3_1))  # ['hello, heaao, hecco, hexao']


# 4. 語法【+】
#    描述 : 它會符合某事物出現 1 次或多次。它適用於任何字母數字字元、\、點和 []。
#    正規表示式 : r”ab+”
#    意思 : index0必須是a，index1必須至少有一個b
#    匹配 : “ab”, “abbbbbbb”
print("----- syntax4 -----")
text4 = r"a, ab ,abbbbb, ac, abc, abbbbc, acc, abdc"
print(re.findall(r"ab+", text4))  # ['ab', 'abbbbb', 'ab', 'abbbb', 'ab']
print(
    re.findall(r"ab+c", text4)
)  # ['abc', 'abbbbc'] => index0必須是a，最後一個index必須是c，中間的index必須是b或沒有b(不能是除了b以外的)
print(
    re.findall(r"[a-c]+", text4)
)  # ['a', 'ab', 'abbbbb', 'ac', 'abc', 'abbbbc', 'acc', 'ab', 'c']

# 5. 語法【\d】
#    描述 : 匹配任何十進制數字的字元(整數0~9)。
#    正規表示式 : r"File\d\d\d"
#    意思 : index0~3必須是File，然後index4~6必須是0~9的整數
#    匹配 : “File100”, “File543”
print("----- syntax5 -----")
text5 = r"File100, File5431, File12, File1e1"
print(re.findall(r"File\d\d\d", text5))  # ['File100', 'File543']
text5_1 = r"08-1234567, 02-7654321 0d-1234567"
print(re.findall(r"0\d-\d{7}", text5_1))  # ['08-1234567', '02-7654321']

# 6. 語法【\D】
#    描述 : 匹配任何非十進制數字的字元。
#    正規表示式 : r”\D\D”
#    意思 : index0~1必須是非0~9數字的字元
#    匹配 : “He”, “we”, “?+”
print("----- syntax6 -----")
text6 = r"File100, File5431, File12, File2e2"
print(re.findall(r"File\d\D\d", text6))  # ['File2e2']


# 7. 語法【{m}】
#    描述 : 指定正好有 m 個 RE 副本。例如，r“\d{3}”與r“\d\d\d”相同。它適用於任何字母數字字元、\、點和 []。
#    正規表示式 : r”Hello\d{3}”
#    意思 : index0~4必須是Hello，index5,6,7必須是0~9的整數
#    匹配 : “Hello100”, “Hello456”
print("----- syntax7 -----")
text7 = r"Hello900, Hello2e2, Hello22"
print(re.findall(r"Hello\d{3}", text7))  # ['Hello900']

# 8. 語法【{m,n}】
#    描述 : 指定 RE 的 m 到 n 個副本。
#    正規表示式 : r” Hello\d{1,3}”
#    意思 : index0~4必須是Hello，index5要需1~3個0~9個整數
#    匹配 : “Hello3”, “Hello58”
print("----- syntax8 -----")
text8 = r"Hello900, Hello2e2, Hello22, Hello333333, Hello"
print(
    re.findall(r"Hello\d{1,3}", text8)
)  # ['Hello900', 'Hello2', 'Hello22', 'Hello333']


# 9. 語法【{m,}】
#    描述 : 指定 m 個或更多 RE 副本。
#    正規表示式 : r” Hello\d{1,}”
#    意思 : index0~4必須是Hello，index5要需至少1個0~9個整數
#    匹配 : “Hello3”, “Hello588873”
print("----- syntax9 -----")
text9 = r"Hello900, Hello2e2, Hello22, Hello333333, Hello"
print(
    re.findall(r"Hello\d{1,}", text9)
)  # ['Hello900', 'Hello2', 'Hello22', 'Hello333333']


# 10. 語法【\w】
#    描述 : 匹配任何字母數字字元。
#    正規表示式 : r”\w-\w”
#    意思 : index0,2必須是字母或數字(非特殊符號)，index1必須是-
#    匹配 : “4-3”, “4-t”, “a-b”
print("----- syntax10 -----")
text10 = f"4-3, 4-t, t-4, a-b, !-b, 我-b"
print(re.findall(r"\w-\w", text10))  # ['4-3', '4-t', 't-4', 'a-b', '我-b']


# 11. 語法【\W】
#    描述 : 匹配任何非字母數字字符，例如 +、? 或 !
#    正規表示式 : r”\W”
#    匹配 : “+”
print("----- syntax11 -----")
text11 = f"+ = - ! a bn"
print(re.findall(r"\W", text11))  # ['+', ' ', '=', ' ', '-', ' ', '!', ' ', ' ']


# 12. 語法【\s】
#    描述 : 匹配空格。
#    正規表示式 : r”a\sb\sc”
#    匹配 : “a b c” (指匹配這個)
print("----- syntax12 -----")
text12 = f"a b c d e abc"
print(re.findall(r"a\sb\sc", text12))  # ['a b c']


# 13. 語法【\S】
#    描述 : 匹配非空白。
#    正規表示式 : r”\S\S\S\S\S”
#    匹配 : “AKB48”
print("----- syntax13 -----")
text13 = f"a b c d e abc adbec"
print(re.findall(r"a\Sb\Sc", text13))  # ['adbec']


# 14. 語法【\.】
#    描述 : 由於點在 RE 中具有特殊含義，因此我們使用 \.查找字串中的點。
#    正規表示式 : r"\.*""
#    匹配 : “”, “.”, “…….”
print("----- syntax14 -----")
text14 = f".. . ... ..... "
print(re.findall(r"\.+", text14))  # ['..', '.', '...', '.....']


# 15. 語法【\b】
#    描述 : 符合單字開頭或結尾的空字串。
#    正規表示式 : r“\bhello”
#    意思 : index0~4必須是hello
#    匹配 : “hello”
print("----- syntax15 -----")
text15 = f"This island is beautiful"
print(
    re.findall(r"\bis", text15)
)  # ['is', 'is']，This並沒有被找到，因為開頭是Th，不是empty string
print(
    re.findall(r"is\b", text15)
)  # ['is', 'is']，island並沒有被找到，因為is後面(結尾)不是empty string
print(re.findall(r"\bis\b", text15))  # ['is']，只有is符合，因為前後都是empty string

# 16. 語法【|】
#    描述 : A | B 建立一個與 A 或 B 相符的 RE，其中 A、B 都是 RE。
#    正規表示式 : r”[a-zA-Z]+|[0-9]+”
#    意思 : index0要至少是一個a~Z或是0~9
#    匹配 : “Hello”, “56778”
print("----- syntax16 -----")
text16 = r"Hello, 56778 ..567"
print(re.findall(r"[a-zA-Z]+|[0-9]+", text16))  # ['Hello', '56778', '567']

# 我們也可以使用括號來匹配括號內的任何正規表示式。它將指示一組的開始和結束；
# 透過tuple元組執行配對後可以檢索群組的內容。
phone_text = r"my number is 02-1234567 02-7654321"
phone_regex = r"(0\d{1})-(\d{7})"
result = re.findall(phone_regex, phone_text)
print(result)  # [('02', '1234567'), ('02', '7654321')]
for area_code, number in result:
    print(f"區碼:{area_code} 號碼:{number}")
# 區碼:02 號碼:1234567
# 區碼:02 號碼:7654321
