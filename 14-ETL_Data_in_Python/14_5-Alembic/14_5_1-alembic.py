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
    inspect,
)
from sqlalchemy.orm import Session, declarative_base


# 連結到db_path這個db
db_path = os.path.join(
    os.getcwd(), "14-ETL_Data_in_Python", "14_5-Alembic", "datafile.db"
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
inspector = inspect(engine)
print(inspector)
print(inspector.get_table_names())  # ['people']
# alembic upgrade head之後
# ['address', 'alembic_version', 'people']
# alembic downgrade -1之後
# ['alembic_version', 'people']
