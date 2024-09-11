import sqlite3
import os

# - SQLite3中的遊標是一個幫助執行查詢並從資料庫中取得記錄的物件。呼叫函數cursor.execute()後，我們可以將遊標物件保存在變數result中，然後執行以下操作：

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 1. C(Create) : 創建(參照14_3_1-sqlite_create.py)
cursor.execute(
    """create table people(id integer primary key, name text, age integer)"""
)
cursor.execute(
    """insert into people (name,age)
               values(?,?)""",
    ("John", 20),
)

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


# 2. R(Read) : 讀取
result = cursor.execute("""SELECT * FROM PEOPLE""")
# 2-1. result.fetchmany(n) – 傳回前 n 個元組的清單。
print(result.fetchmany(1))  # [(1, 'John', 20)]

# 2-2. result.fetchall() – 返回元組清單；資料庫中的每一行資料儲存在一個元組中。
print(result.fetchall())  # [(2, 'Jessica', 18), (3, 'Joan', 23)]
print(
    cursor.execute("""SELECT * FROM PEOPLE""").fetchall()
)  # [(1, 'John', 20), (2, 'Jessica', 18), (3, 'Joan', 23)]

# NAME欄位的第二個字元為o的資料，按照ID倒序全部列出
print(
    cursor.execute(
        """SELECT * FROM PEOPLE
                     WHERE SUBSTR(NAME,2,1) = 'o'
                     ORDER BY ID DESC"""
    ).fetchall()
)  # [(3, 'Joan', 23), (1, 'John', 20)]

# 2-3. result.fetchone() – 傳回 SQL 語句的第一個符合項目的元組。
print(
    cursor.execute(
        """SELECT * FROM PEOPLE
                     WHERE SUBSTR(NAME,2,1) = 'o'
                     ORDER BY ID DESC"""
    ).fetchone()
)  # (3, 'Joan', 23)


# 3. U(Update) : 更新(修改)
cursor.execute(
    """UPDATE PEOPLE
    SET NAME = :new_name
    WHERE NAME = :old_name""",
    {"new_name": "Kevin", "old_name": "John"},
)
print(
    cursor.execute("""SELECT * FROM PEOPLE""").fetchall()
)  # [(1, 'Kevin', 20), (2, 'Jessica', 18), (3, 'Joan', 23)]

# 4. D(Delete) : 刪除
cursor.execute(
    """DELETE FROM PEOPLE
               WHERE NAME = :name""",
    {"name": "Kevin"},
)
print(
    cursor.execute("""SELECT NAME,AGE FROM PEOPLE""").fetchall()
)  # [('Jessica', 18), ('Joan', 23)]


# SQL Injection(SQL注入) : SQL注入是一種用於攻擊資料驅動應用程式的程式碼注入技術，其中惡意SQL語句被插入到輸入欄位中以執行
# example : 密碼查詢
cursor.execute("""create table user_data(username text primary key, password text)""")
cursor.execute(
    """INSERT INTO USER_DATA(username,password)
               VALUES('John' , '123'),
               ('Jessica','456')"""
)

want_username = input("請輸入帳號:")
print(
    cursor.execute(
        f"""SELECT * FROM USER_DATA
               WHERE username = '{want_username}'"""
    ).fetchall()
)
# 請輸入帳號:Jessica
# [('Jessica', '456')]

# 請輸入帳號:1' or '1' = '1
# [('John', '123'), ('Jessica', '456')]
# 這樣就所有帳密都被知道了
# 因為execute最後執行的SQL statement為
# SELECT * FROM USER_DATA WHERE username = '1' OR '1' = '1'
# '1' = '1'會為True，所以所有資料都符合WHERE條件

# 使用參數化查詢
print(
    cursor.execute(
        """SELECT * FROM USER_DATA
                     WHERE USERNAME = :username""",
        {"username": want_username},
    ).fetchall()
)
# 請輸入帳號:1' or '1' = '1
# 印出[]
# 因為用參數化的話執行的sql statement為
# SELECT * FROM USER_DATA
# WHERE USERNAME = "'1' or '1' = '1'"
# 他為把1' or '1' = '1當成一個字串，其中的' or就不具備其他意義
conn.commit()
conn.close()
