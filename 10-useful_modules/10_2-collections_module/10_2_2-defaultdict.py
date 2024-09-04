# defaultdict 是字典類別的子類，它會傳回類似字典的物件。
# 字典和 defualtdict 的功能幾乎相同，除了 defualtdict "永遠不會引發 KeyError "之外。它為不存在的鍵提供預設值。
# 為什麼defaultdict是小寫的？這只是不遵循 Python 的指導方針。他們會修復它嗎？我們不知道，但人們已經提交了將名稱更改為 Defaultdict 的請求。希望他們遲早會改變它。

# 語法: defaultdict(default_factory)
# 其中 default_factory 是傳回定義的字典的預設值的fucntion。如果該參數不存在，則字典將引發 KeyError。
from collections import defaultdict


# factory fcuntion
def default_factory():
    return "這個key未被定義"


# 用lambda expression來定義default_factory參數，因為沒有parameter所以直接: return值就好了
person1 = defaultdict(lambda: "This key is not defined")
person1["job"] = "teacher"
person1["name"] = "Jessica"
person1["sex"] = "female"
print(
    f"person1的姓名:{person1['name']}，性別:{person1['sex']}，職業:{person1['job']}，年齡:{person1['age']}"
)
# person1的姓名:Jessica，性別:female，職業:teacher，年齡:This key is not defined
