import datetime
from typing import Optional  # 導入 Optional，用於定義可選的類型
from sqlalchemy import (
    Integer,  # 導入整數型別
    String,  # 導入字串型別
    DateTime,  # 導入日期時間型別
)
from sqlalchemy.orm import (
    mapped_column,  # 導入映射欄位的函數
)
from typing_extensions import Annotated  # 導入 Annotated，用於註解型別


# 定義一個基類型別，提供常用的資料型別映射
class BaseType:
    # 定義整數主鍵，自動增量且唯一
    int_primary_key = Annotated[
        int, mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    ]
    # 定義最大長度為 30 的字串
    str_30 = Annotated[str, mapped_column(String(30))]
    # 定義最大長度為 50 的字串
    str_50 = Annotated[str, mapped_column(String(50))]
    # 定義可選的最大長度為 50 的字串
    optional_str_50 = Annotated[Optional[str], mapped_column(String(50), nullable=True)]
    # 定義可選的最大長度為 100 的字串
    optional_str_100 = Annotated[
        Optional[str], mapped_column(String(100), nullable=True)
    ]
    # 定義更新時間，預設為當前時間，並在更新時自動更改
    update_time = Annotated[
        datetime.datetime,
        mapped_column(
            DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
        ),
    ]
