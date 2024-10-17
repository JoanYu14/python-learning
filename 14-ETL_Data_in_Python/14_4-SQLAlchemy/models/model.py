from datetime import date  # 從 datetime 模組導入 date 類型
from sqlalchemy import Date, ForeignKey  # 導入日期型別
from sqlalchemy.orm import (
    Mapped,  # 導入 Mapped 類別，用於映射資料庫欄位
    mapped_column,  # 導入映射欄位的函數
    relationship,  # 導入關聯函數，用於定義 ORM 之間的關係
    declarative_base,  # 導入聲明式基類，用於創建 ORM 類別
)
from typing import Optional  # 導入 Optional，用於定義可選的類型

from .base import BaseType

# from .item import Item

Base = declarative_base()


# 定義 User 類別，對應到資料庫中的 User 資料表
class User(Base):
    __tablename__ = "User"  # 資料表名稱設定為 "User"

    # 定義資料表欄位
    id: Mapped[BaseType.int_primary_key]  # 使用基類型別中的主鍵定義
    password: Mapped[BaseType.str_50]  # 密碼欄位，最大長度 50 的字串
    name: Mapped[BaseType.str_30]  # 姓名欄位，最大長度 30 的字串
    age: Mapped[int]  # 年齡欄位，整數型別
    avatar: Mapped[BaseType.optional_str_100]  # 可選的頭像欄位，最大長度 100 的字串
    birthday: Mapped[date] = mapped_column(Date)  # 生日欄位，使用日期型別
    email: Mapped[BaseType.str_50]  # 郵箱欄位，最大長度 50 的字串
    create_time: Mapped[BaseType.update_time]  # 創建時間欄位，使用更新時間的定義

    # 定義與 Item 類別的關聯，一個 User 可以擁有多個 Item
    items: Mapped[list["Item"]] = relationship(
        "Item",  # 相關聯的 Item 類別名稱
        back_populates="user",  # 反向關聯，指向 User 類別的 items
        cascade="all, delete-orphan",  # 當 User 被刪除時，相關的 Item 也會被刪除
        lazy="select",  # 使用延遲加載方式以提高效能
        order_by="Item.name",  # 根據 Item 名稱排序
    )

    def __init__(
        self,
        password: str,  # 密碼
        name: str,  # 姓名
        age: int,  # 年齡
        avatar: Optional[str],  # 可選的頭像
        birthday: date,  # 生日
        email: str,  # 郵箱
    ) -> None:
        # 初始化方法，用於創建 User 物件
        # 密碼應在存儲到資料庫之前進行雜湊處理，這裡僅用於演示
        self.password = password
        self.name = name
        self.age = age
        self.avatar = avatar
        self.birthday = birthday
        self.email = email

    def __repr__(self) -> str:
        # 定義物件的字串表示形式，便於調試和顯示
        return f"<User(id={self.id}, name={self.name}, age={self.age}, email={self.email})>"


# 定義 Item 類別，對應到資料庫中的 Item 資料表
class Item(Base):
    __tablename__ = "Item"  # 資料表名稱
    id: Mapped[BaseType.int_primary_key]  # 使用基類型別中的主鍵定義
    name: Mapped[BaseType.str_50]  # 名稱，最大長度 50 的字串
    price: Mapped[float]  # 價格，浮點數型別
    brand: Mapped[BaseType.str_30]  # 品牌，最大長度 30 的字串
    description: Mapped[BaseType.optional_str_100]  # 可選的描述，最大長度 100 的字串
    create_time: Mapped[BaseType.update_time]  # 創建時間，使用更新時間定義
    last_login: Mapped[BaseType.update_time]  # 最後登入時間，使用更新時間定義

    # 定義外鍵，連結到 User 資料表
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete="cascade"))
    # 定義與 User 類別的關聯，指向 User 類別
    user: Mapped["User"] = relationship("User", back_populates="items")

    def __init__(self, name, price, brand, description, user_id):
        self.name = name
        self.price = price
        self.brand = brand
        self.description = description
        self.user_id = user_id

    def __repr__(self) -> str:
        # 定義物件的字串表示形式，便於調試和顯示
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, brand={self.brand},description={self.description},user_id={self.user_id})>"
