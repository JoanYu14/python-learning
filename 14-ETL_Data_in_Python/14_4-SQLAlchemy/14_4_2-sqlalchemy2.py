from sqlalchemy import create_engine, text, delete  # 導入創建資料庫引擎的函數
from sqlalchemy.orm import Session, declarative_base  # 導入會話類別，用於與資料庫交互
import datetime

# 要cd到14-ETL_Data_in_Python目錄下執行此.py才能正確import
from models.model import Item, User


# 創建 SQLite 資料庫引擎，使用記憶體中的資料庫
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


Base = declarative_base()
Base.metadata.create_all(bind=engine, tables=[User.__table__, Item.__table__])
session = Session(engine)


def create_user_and_item(user_info, item_info):
    # 定義一個內部函數來創建 item
    def create_item(item, user_id):
        # 打印出正在使用的 user_id
        print("user_id為", user_id)
        # 創建 Item 物件，並將 user_id 傳入
        item_obj = Item(
            name=item["name"],
            price=item["price"],
            brand=item["brand"],
            description=item["description"],
            user_id=user_id,  # 使用傳入的 user_id
        )
        session.add(item_obj)  # 將 item 物件加入到 session
        print("item 已增加")  # 提示 item 已成功增加
        session.commit()  # 提交事務

    # 創建 User 物件
    user_obj = User(
        password=user_info["password"],
        name=user_info["name"],
        age=user_info["age"],
        birthday=user_info["birthday"],
        email=user_info["email"],
        avatar=user_info["avatar"],
    )

    session.add(user_obj)  # 添加 User 物件到 session
    session.commit()  # 提交 User 物件到數據庫

    # 使用 list(map(...)) 確保每個 item 都被創建
    list(map(lambda item: create_item(item, user_obj.id), item_info))

    return "OK"  # 返回成功的提示


# 創建第一個 user 及其 items
create_user_and_item(
    user_info={
        "password": "123",
        "name": "John",
        "age": 20,
        "birthday": datetime.datetime(year=2004, month=1, day=10),
        "email": "123@gmail.com",
        "avatar": None,
    },
    item_info=[
        {
            "name": "test1",
            "price": 123,
            "brand": "test_brand1",
            "description": "this is description1",
        },
        {
            "name": "test2",
            "price": 345,
            "brand": "test_brand2",
            "description": "this is description2",
        },
    ],
)

# 創建第二個 user 及其 items
create_user_and_item(
    user_info={
        "password": "12345",
        "name": "Kevin",
        "age": 24,
        "birthday": datetime.datetime(year=2000, month=1, day=10),
        "email": "456@gmail.com",
        "avatar": None,
    },
    item_info=[
        {
            "name": "test2-1",
            "price": 333,
            "brand": "test_brand2-1",
            "description": "this is description2-1",
        },
        {
            "name": "test2-2",
            "price": 777,
            "brand": "test_brand2-2",
            "description": "this is description2-2",
        },
        {
            "name": "test2-3",
            "price": 888,
            "brand": "test_brand2-3",
            "description": "this is description2-3",
        },
    ],
)

# 查詢所有 User
result = session.query(User).all()
for counter, r in enumerate(result):
    print(f"第{counter+1}個User的資料為{r}")
# 顯示所有 User 的資料

# 查詢所有 Item
query_result = session.query(Item).all()
for counter, r in enumerate(query_result):
    print(f"第{counter+1}個Item的資料為{r}")
# 顯示所有 Item 的資料

# 查詢 Kevin 的所有 Items
kevin_item_result = session.query(Item).filter_by(user_id=2).all()
for counter, r in enumerate(kevin_item_result):
    print(f"第{counter+1}個Kevin的Item的資料為{r}")
# 顯示 Kevin 的 Items

# 查詢名為 Kevin 的 User
kevin_user = session.query(User).filter_by(name="Kevin").first()

# 刪除 Kevin 的資料，Kevin的Item會一起被刪除
session.delete(kevin_user)  # 將查詢到的 User 物件刪除
session.commit()  # 提交更改

# 查詢所有 Items 以確認 Kevin 的 Items 是否已被刪除
new_query_result = session.query(Item).all()
for counter, r in enumerate(new_query_result):
    print(f"第{counter+1}個Item的資料為{r}")

# user_id為2的Item全部被刪除了
# 第1個Item的資料為<Item(id=1, name=test1, price=123.0, brand=test_brand1,description=this is description1,user_id=1)>
# 第2個Item的資料為<Item(id=2, name=test2, price=345.0, brand=test_brand2,description=this is description2,user_id=1)>


# ======= Core語法 ========
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT NAME,PRICE,DESCRIPTION FROM ITEM WHERE USER_ID = :user_id"),
        [{"user_id": 1}],
    )
    for r in result:
        print(f"name:{r.name}, price:{r.price}, description:{r.description}")
        # name:test1, price:123.0, description:this is description1
        # name:test2, price:345.0, description:this is description2


# 刪掉Item table中所有price大於300的Item
stmt = delete(Item).where(Item.price > 300)
session.execute(stmt)
session.commit()
# 查詢所有 Item
query_result = session.query(Item).all()
for counter, r in enumerate(query_result):
    print(f"第{counter+1}個Item的資料為{r}")
