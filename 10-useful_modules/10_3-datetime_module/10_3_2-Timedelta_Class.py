# 每個 timedelta 物件代表一個持續時間，即兩個日期或時間之間的差異。
# 通常，我們會使用唯讀實例屬性 days 和一個實例method total_seconds() 來取得兩個日期時間物件之間的天數或秒數差異。
import datetime

now = datetime.datetime.now()
oneday = datetime.datetime(2020, 1, 1)
diff = now - oneday
print(diff)
print(type(diff))  # <class 'datetime.timedelta'>

# timedelta read-only attribute, method
print(f"現在與2020/1/1 00:00:00相隔{diff.days}天")  # 1708
print(f"現在與2020/1/1 00:00:00相隔{diff.total_seconds()}秒")

# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
gap = datetime.timedelta(3)
print(f"三天後的時間為{now+gap}")  # 三天後的時間為2024-09-07 15:50:31.456390
