# 1. 不同的 SQL 資料庫以略有不同的方式實作 SQL。這意味著，例如，我們為 SQLite 編寫的 SQL 語句不一定總是適用於 MySQL。本地開發是使用 sqlite3 完成的，但生產是在 MySQL 或 PostgreSQL 中完成的。然後，我們必須相應地切換SQL語句，這將是非常繁瑣的。如果我們有500條SQL語句，我們就得一一修改、測試。
# 2. 在我們的程式碼中包含 SQL 語句會使我們的程式碼更難以維護，特別是當我們有許多 SQL 語句時。例如，如果我將表名從 people 更改為 user，那麼我們必須繼續更改所有 SQL 語句。我們應該有一些簡單的東西來為我們產生 SQL 語句
# 解決方案是物件關聯映射 (Object Relational Mapper -ORM)，它將關聯式資料庫類型和結構轉換或映射為 Python 中的物件。
# pip install sqlalchemy

# create_engine 用來創建資料庫引擎，通過該引擎與資料庫進行連接
# select 是 SQLAlchemy 中用來構造 SQL SELECT 查詢的功能
# MetaData 是一個元數據對象，用於存儲表的結構與資料庫之間的映射關係
# Table 用於定義資料庫中的表結構，包括表名、列定義等
# Column 用於定義表中的每一列，並且可以指定列的屬性如類型、主鍵等
# Integer 是用來指定資料庫列的數據類型，這裡表示整數
# String 是另一個資料庫列的數據類型，這裡表示字符串
# sessionmaker 是用來創建資料庫會話的工具，會話可以用來管理資料庫的查詢和操作
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
