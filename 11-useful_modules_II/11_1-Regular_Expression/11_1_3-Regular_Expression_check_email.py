import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
# ^代表撇除
regex2 = r"[^@]+@[^@]+\.[^@]+"


def check_mail(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def check_mail2(email):
    if re.fullmatch(regex2, email):
        return True
    else:
        return False


print(check_mail("123@gmail.com"))  # True
print(check_mail("123@yahoo.com.tw"))  # True
print(check_mail("123@gmail"))  # False
print(check_mail("@gmail.com"))  # False

print(check_mail2("123@gmail.com"))  # True
print(check_mail2("123@yahoo.com.tw"))  # True
print(check_mail2("123@gmail"))  # False
print(check_mail2("@gmail.com"))  # False
