a = int(input("請輸入您的年齡："))

if a < 0:
    print("請輸入正確的年齡")
elif 18 <= a < 65:
    print("票價為200元")
elif a < 18:
    print("票價為50元")
else:
    print("票價為100元")


if not a:
    print("Falsy Value")
else:
    print("Truthy Value")