for i in range(0,3):
    for j in range(0,3):
        if i==0:
            print("i=0") # 當i為0時會print1次這個，代表j迴圈只執行了一次
            break
        print(i,j)