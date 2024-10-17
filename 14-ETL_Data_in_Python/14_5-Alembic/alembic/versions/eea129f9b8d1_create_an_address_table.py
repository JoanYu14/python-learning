"""
create an address table

Revision ID: eea129f9b8d1
Revises: 
Create Date: 2024-10-17 15:40:15.897374

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "eea129f9b8d1"  # 這是 Alembic 生成的修訂版本 ID，用來唯一標識這個修訂。
down_revision: Union[str, None] = (
    None  # 該修訂的上一次修訂 ID，因為這是新建的修訂，沒有上一次修訂，故為 None。
)
branch_labels: Union[str, Sequence[str], None] = (
    None  # 如果你使用了分支標籤，這裡可以定義分支標籤，這裡為 None。
)
depends_on: Union[str, Sequence[str], None] = (
    None  # 表示這個修訂是否依賴於其他修訂，這裡為 None。
)


# `upgrade` 函數是用來處理數據庫升級的邏輯
def upgrade() -> None:
    # 使用 Alembic 的 `op.create_table` 函數來創建 `address` 表
    op.create_table(
        "address",  # 表名為 'address'
        # 定義 `id` 欄位，使用 Integer 類型，且設定為主鍵
        sa.Column("id", sa.Integer, primary_key=True),
        # 定義 `address` 欄位，類型為 String，長度限制為 50，且該欄位不能為空 (nullable=False)
        sa.Column("address", sa.String(50), nullable=False),
        # 定義 `city` 欄位，類型為 String，長度限制為 50，且該欄位不能為空
        sa.Column("city", sa.String(50), nullable=False),
        # 定義 `state` 欄位，類型為 String，長度限制為 50，且該欄位不能為空
        sa.Column("state", sa.String(50), nullable=False),
    )


# `downgrade` 函數是用來處理數據庫回退的邏輯
def downgrade() -> None:
    # 使用 Alembic 的 `op.drop_table` 函數來刪除 `address` 表
    op.drop_table("address")
