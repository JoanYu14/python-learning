# string.encode(encoding) – 傳回字串根據編碼對應到的位元組。
# byte.decode(encoding) – 傳回位元組根據編碼映射到的字串。
unicode_string = "中"
utf_bytes = unicode_string.encode()
print(utf_bytes)  # b'\xe6\x88\x91'
print(utf_bytes.decode())  # 中
# e4 => 11100100
# b8 => 10111000
# ad => 10101101
# 透過e4(11100100)我們得知這3個bytes要一起讀
# 起始bytes接續的後面的bytes都是10xx xxxx開頭的，可以看到要一起讀的後面2個bytes的開頭都是10
