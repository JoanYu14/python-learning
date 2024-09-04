# Named tuples(命名元組)基本上是易於創建的輕量級物件類型。
# 可以使用類似物件的變數取消引用或標準元組語法來引用命名元組實例。
# （基本上，這意味著我們給元組鍵，以便可以透過鍵或索引存取元組中的內容。這就像字典和元組的混合體。）
# 就是我給tuple的每個值一個name，這樣我們就可以用name來獲取tuple內的值，而不需靠index
from collections import namedtuple
from math import sqrt

# namedtuple會創造一個Class
# 所以當你要創建一個沒有任何Method的Class的話就很適合用namedtuple創建
Point = namedtuple("Point", ["x", "y"])
print(Point)  # <class '__main__.Point'>
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_length = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
line_length_namedtuple = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
print(line_length)  # 3.8078865529319543
print(line_length_namedtuple)  # 3.8078865529319543
