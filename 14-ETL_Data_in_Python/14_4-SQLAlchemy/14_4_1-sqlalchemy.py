import os
from sqlalchemy import (
    create_engine,
    select,
    update,
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import Session, declarative_base


# 連結到db_path這個db
db_path = os.path.join(
    os.getcwd(), "14-ETL_Data_in_Python", "14_4-SQLAlchemy", "datafile.db"
)
# conn = sqlite3.connect(db_path) # 舊的sqlite連接方式，現在改用SQLAlchemy
engine = create_engine("sqlite:///%s" % db_path)  # 創建一個SQLite資料庫的引擎

# 建立MetaData對象，用於描述資料庫中的結構（例如表、列）
metadata = MetaData()

# 使用Table對象設定Metadata，定義一個名為people的表
people = Table(
    "people",
    metadata,
    Column("id", Integer, primary_key=True),  # 主鍵id
    Column("name", String),  # 名稱列
    Column("count", Integer),  # 計數列
)

# 創建一個會話物件(session object)，與資料庫連接，它綁定了引擎
session = Session(engine)

# 在資料庫中建立表，若不存在則創建
metadata.create_all(engine)

# 構建一個插入語句，插入一筆數據
sql_statement1 = people.insert().values(name="Bob", count=10)
print(sql_statement1)  # INSERT INTO people (name, count) VALUES (:name, :count)

# 執行插入語句
session.execute(sql_statement1)

# 批量插入多筆數據
session.execute(
    people.insert(), [{"name": "Joan", "count": 23}, {"name": "Jessica", "count": 20}]
)

# 提交變更到資料庫
session.commit()

# 執行查詢，從people表中選取所有數據
result = session.execute(select(people))
for row in result:
    print(row)  # 會輸出表中的每一行數據

# 因為 session.execute(select(people)) 返回的是一個 CursorResult，而不是一個可以調用 .where() 的查詢對象
print()

# 使用where子句過濾查詢，查詢name為Joan的記錄
where_result = session.execute(select(people).where(people.c.name == "Joan"))
for row in where_result:
    print(row)  # 輸出name為Joan的記錄

# 使用update語句更新name為Jessica的記錄的count欄位
session.execute(update(people).values(count=100).where(people.c.name == "Jessica"))

# 查詢name為Jessica的記錄，確認是否已更新
query_result = session.execute(select(people).where(people.c.name == "Jessica"))
for row in query_result:
    print(row)  # 輸出更新後的Jessica記錄

# 使用ORM定義Table Metadata，這是一個更高層級的SQLAlchemy用法
Base = declarative_base()  # 創建一個ORM基類


# 定義People類，對應到資料庫中的people表
class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)  # 主鍵id
    name = Column(String(30))  # 名稱列
    count = Column(Integer)  # 計數列

    def __repr__(self):  # 定義字串表示，方便調試時輸出對象資訊
        return f"People(id={self.id!r}, name={self.name!r}, count={self.count})"


# 創建兩個新的人物對象
new1 = People(name="Kevin", count=11)
new2 = People(name="Peter", count=33)

# 將新對象添加到當前會話中，等待提交
session.add(new1)
session.add(new2)

# 提交變更到資料庫
session.commit()

# 查詢name為Kevin的第一個記錄
kevin = session.query(People).filter_by(name="Kevin").first()
print(kevin)  # 輸出Kevin的記錄，類似 People(id=49, name='Kevin', count=11)

# 修改Kevin的count欄位值
kevin.count = 99
print(kevin)  # 輸出修改後的Kevin記錄，類似 People(id=49, name='Kevin', count=99)

# 刪除Kevin的記錄
session.delete(kevin)

# 再次查詢Kevin
for row in session.query(People).filter_by(name="Kevin").all():
    print(row)

# id為49的已被刪除
# People(id=54, name='Kevin', count=11)
# People(id=59, name='Kevin', count=11)
# People(id=64, name='Kevin', count=11)
# People(id=69, name='Kevin', count=11)
# People(id=74, name='Kevin', count=11)
# People(id=79, name='Kevin', count=11)
# People(id=84, name='Kevin', count=11)
# People(id=89, name='Kevin', count=11)
