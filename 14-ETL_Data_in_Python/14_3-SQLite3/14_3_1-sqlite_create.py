# 1. SQLite 是 Python 標準函式庫的一部分；它可以在我們需要資料庫的任何地方使用，而無需擔心添加依賴項。
# 2. SQLite 將其所有記錄儲存在本機檔案中（即，它是無伺服器的），因此它不需要客戶端和伺服器
import sqlite3
import os

# 1. sqlite3.connect(filename.db) - 連線到 .db 檔案並傳回 Connection 物件。如果 filename.db 不存在，則會建立一個。如果檔案名稱是“:memory:”，那麼資料庫將在我們的 RAM 中創建，而不是在硬碟中。
# 若是存在RAM裡面的話，程式碼執行完這個database就會消失。如果存在硬碟的話，既使電腦關機，資料也還會在。

# 將SQLite資料存到硬碟(資料持久化)
datafile_path = os.path.join(
    os.getcwd(), "14-ETL_Data_in_Python", "14_3-SQLite3", "datafile.db"
)
conn = sqlite3.connect(datafile_path)

# 將SQLite資料存在RAM中(資料在程式執行結束後就會消失)
# conn = sqlite3.connect(":memory:")

# 2. conn.cursor() – 傳回一個遊標object，它可以操作資料庫。
cursor = conn.cursor()
# print(cursor) # <sqlite3.Cursor object at 0x000001F0FA838B20>

# 3. cursor.execute(SQLStatement, object) – 執行 SQL 語句並傳回遊標物件。第二個object是可選的。
cursor.execute(
    """create table people(id integer primary key, name text, age integer)"""
)
# 3_1:以順序的方式參數化執行SQL statement
# ?會依序對上第二個參數的tuple的值，這是參數化的方式，可以防止SQL injection
cursor.execute(
    """insert into people (name,age)
               values(?,?)""",
    ("John", 20),
)

# 3_2:以dictionary對照名稱的方式參數化執行SQL statement
# :parameter_name會去對應第二個參數中dic的parameter_name這個key的value
cursor.execute(
    """insert into people (name,age)
               values(:username,:age)""",
    {"username": "Jessica", "age": 18},
)

cursor.execute(
    """INSERT INTO PEOPLE(NAME, AGE)
               VALUES(:name, :age)""",
    {"name": "Joan", "age": 23},
)
# 4. conn.commit() – 將變更儲存到資料庫。預設情況下，除非我們執行 conn.commit() 方法，否則對資料庫所做的任何更改都不會被儲存。每次提交也是資料庫的歷史記錄。這意味著，如果某個變更發生錯誤，那麼我們可以回滾到提交的最後一個版本。
conn.commit()

# 5. conn.close() – 關閉資料庫連線。
conn.close()
