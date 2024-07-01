a = "a"
#在函數定義內部（無論發生在哪裡），如果我們對變數進行賦值（並且不使用 global 關鍵字），Python 將自動建立該局部變數。
def change(x):
    if x:
        # 只要有a=?，那python就會製作localVar a，不管if是否有被執行
        a = "changed a"
    print(a)

change(True) # changed a
#change(False) # UnboundLocalError: local variable 'a' referenced before assignment，因為if沒被執行，所以a已經建立但無賦值
