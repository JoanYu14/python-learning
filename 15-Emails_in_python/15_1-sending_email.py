import smtplib
import getpass

# 此方法傳回一個封裝了 SMTP 連線的 SMTP 實例。它具有支援全部 SMTP 和 ESMTP 操作的方法。
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)

# 1.ehlo() : 向 ESMTP 伺服器表明您的身分。
smtp_obj.ehlo()
# print(
#     smtp_obj.ehlo()
# )
# # (250, b'smtp.gmail.com at your service, [202.39.222.4]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

# 2.starttls() - 將 SMTP 連線置於 TLS（傳輸層安全）模式。隨後的所有 SMTP 命令都將被加密。
smtp_obj.starttls()

# 3.login(使用者名稱, 密碼) - 登入需要驗證的 SMTP 伺服器。
# 這邊要去Google帳號申請應用程式密碼
username = input("請輸入gmail帳號:")
password = getpass.getpass("請輸入密碼:")
print(smtp_obj.login(username, password))  # (235, b'2.7.0 Accepted')

# 4.smtp_obj.sendmail(from_address, to_address, msg)
# 寄出email
print(
    smtp_obj.sendmail(username, username, "Python Send Email Test")
)  # {} 得到這個代表信件已寄出
smtp_obj.quit()  # 停止smtp session
