# import數學模組
# import是Python中用來引入其他模組或套件的關鍵字。通過使用import，你可以將其他Python檔案中定義的函數、類別、變數等引入到當前的Python環境中，以便在目前的檔案中使用。
# 舉例來說，如果有一個名為math的模組，其中定義了數學相關的函數和常數，你可以通過import math將它引入到當前的Python程式中。接著就可以使用math模組中的函數和常數了，例如使用math.sqrt()來計算平方根。
# 除了最基本的import math之外，還有其他一些引入模組的方式，包括：
# 引入特定模組成員：有時你可能只需要引入模組中的部分成員，而不是整個模組。這時可以使用from module_name import name的語法，例如from math import sqrt只引入math模組中的sqrt函數。
# 給模組起別名：有些模組的名稱可能比較長或難以記憶，可以為它們指定一個別名來簡化使用。例如import math as m，然後就可以用m.sqrt()來呼叫sqrt函數。
# 引入模組中的所有成員：雖然這種方式不太推薦，但是可以使用from module_name import *的方式引入模組中的所有成員。這種方式可能會導致命名衝突或者其他不可預測的問題，因此在正式環境中不建議使用。
# import語句通常放在Python檔案的頂部，用於在檔案的其餘部分中引入的模組。
import math

# 常數
print("e:", math.e)  # 自然對數的底數 => 2.718281828459045
print("pi:", math.pi)  # 圓周率 => 3.141592653589793

# 方法
num = 4.7
print(f"floor({num}):", math.floor(num))  # 向下取整 => 4
print(f"ceil({num}):", math.ceil(num))  # 向上取整 => 5

num = -4.7
print(f"floor({num}):", math.floor(num))  # 向下取整 => -5
print(f"ceil({num}):", math.ceil(num))  # 向上取整 => -4

num = 16
print(f"sqrt({num}):", math.sqrt(num))  # 平方根 => 4.0

num = 2
print(f"sqrt({num}):", math.sqrt(num))  # 平方根 => 1.4142135623730951

print("float(1)=>{answer}".format(answer=math.isnan(num)))
print("float(1)=>{answer}".format(answer=math.isnan(1*"1")))