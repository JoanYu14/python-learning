import imaplib
import getpass
import email as em
import os

# 透過指定連接埠與主機建立連線來建立並傳回 IMAP4_SSL 實例。它使用安全的 SSL 連線。
# SSL 的意思是安全通訊端層，SSL 使用對稱加密技術。用於實現 SSL 的最廣泛使用的對稱演算法是 AES-128、AES-192 和 AES-256。與SSL相比，HTTPs使用RSA演算法，即非對稱加密演算法。
M = imaplib.IMAP4_SSL("imap.gmail.com")
username = input("請輸入gmail帳號:")
password = getpass.getpass("請輸入密碼:")

# 1. M.login(電子郵件、密碼)` : 登入需要驗證的電子郵件伺服器。
print(
    M.login(username, password)
)  # ('OK', [b'{your_login_username} authenticated (Success)'])

# 2. M.list()` :傳回一個元組，其中包含帳戶的不同資料夾的訊息，例如收件匣、垃圾桶、草稿。
print(M.list())

# 3. M.select(str)` : 選擇要處理的 str 資料夾。
M.select("inbox")

# 4. M.search(None, criteria)` : 根據條件搜尋電子郵件，並傳回一個元組，其中包含符合條件的電子郵件 ID 資訊。
# 找到從username寄來的信
# print(M.search(None, f"FROM {username}"))  # ('OK', [b'9 19 73'])
result, ids = M.search(None, f"FROM {username}")
# 將字節字符串轉換為正常字符串並分割
ids_str = ids[0].decode()  # 將 b'9 19 73' 轉換為 '9 19 73'
ids_list = ids_str.split()  # 以空格拆分為列表 ['9', '19', '73']

# 選取第一封郵件的 ID，並執行 fetch 命令
email_id = ids_list[2]  # 比如我們想取第三封郵件的 ID '9'

# 5. M.fetch(id, "(RFC822)")` : 根據 id 取得電子郵件的內容。 RFC822 意味著我們正在獲取由標頭字段和訊息正文組成的電子訊息。
# print(M.fetch(email_id, "(RFC822)"))  # 信的內容
result, content = M.fetch(email_id, "(RFC822)")
raw_content = content[0][1]
email_content = raw_content.decode("utf-8")
email_message = em.message_from_string(email_content)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
        with open(
            os.path.join(os.getcwd(), "15-Emails_in_python", "email_content.txt"),
            mode="wb",
        ) as f:
            f.write(body)
