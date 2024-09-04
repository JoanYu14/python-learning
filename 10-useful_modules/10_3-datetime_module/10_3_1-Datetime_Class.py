# datetime Class用於處理日期時間物件。 datetime 物件包含日期和時間的所有資訊。年、月、日、小時、分鐘、秒和微秒都可以在日期時間物件中使用。
import datetime

print(type(datetime))  # <class 'module'>
print(type(datetime.datetime))  # <class 'type'>

# datetime module的datetime Class的.now()這個static method會return當前日期時間
print(
    type(datetime.datetime.now())
)  # <class 'datetime.datetime'> => datetime module裡的datetime class，不是string
now_dt = datetime.datetime.now()
print(now_dt)  # 2024-09-04 13:59:35.432450
print(
    f"當前年:{now_dt.year}，月:{now_dt.month}，日:{now_dt.day}，小時:{now_dt.hour}，分鐘:{now_dt.minute}，秒:{now_dt.second}，毫秒:{now_dt.microsecond}，時間:{now_dt.time()}"
)  # 當前年:2024，月:9，日:4，小時:13，分鐘:59，秒:35，毫秒:432450，時間:13:59:35.432450

# 要建立我們自己的datetime object，我們只需呼叫datetime Class的建構函數：
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
# 需要year、month和day參數。其餘的都是可選的。
mydt_obj = datetime.datetime(
    year=2001,
    month=1,
    day=4,
)

print(now_dt - mydt_obj)  # 8644 days, 14:06:20.067486


# 對於每個datetime object， strftime(format) 方法用於將某些資訊提取為其字串表示形式。 （strftime代表時間字串）
# %A會return當天是星期幾
print(mydt_obj.strftime("%A"))  # Thursday
print(mydt_obj.strftime("%Y/%m/%d"))  # 2001/01/04
print(now_dt.strftime("當前時間%H:%M:%S"))  # 當前時間14:11:43
