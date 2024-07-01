#print(10/0) # ZeroDivisionError: division by zero任何數除以0都無意義(JS的話結果會是infinity)
if 3 or (10/0):
    print("沒有執行10/0") # 因為3就為True了，所以Python根本部會去執行10/0
