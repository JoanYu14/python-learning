# 現在，我們將編寫一個 Tic Tac Toe 遊戲
# 該遊戲將要求來自終端的用戶輸入，並在每次提供用戶輸入時檢查是否有人贏得遊戲。您（可能）可以按照以下步驟操作：
# 顯示網格
# 接受使用者輸入
# 更新遊戲網格
# 遊戲獲勝檢查演算法
# 完善遊戲機制

space = [str(x) for x in range(0,9)]
win = False
while not win:
    for i in range(3):
        print(" - - -")
        print(f'|{space[i*3+0]}|{space[i*3+1]}|{space[i*3+2]}|')
    if (space[0]==space[4]==space[8]=="X"):
        print("玩家2獲勝")
        win = True
        break
    elif(space[0]==space[4]==space[8]=="O"):
        print("玩家1獲勝")
        win = True   
        break    
    elif(space[2]==space[4]==space[6]=="O"):
        print("玩家1獲勝")
        win = True      
        break
    elif(space[2]==space[4]==space[6]=="X"):
        print("玩家2獲勝")
        win = True   
        break
    for j in range(3):
        # 橫排
        if(space[j*3+0]==space[j*3+1]==space[j*3+2]=="X"):
            print("玩家2獲勝")
            win = True
            break
        elif(space[j*3+0]==space[j*3+1]==space[j*3+2]=="O"):
            print("玩家1獲勝")
            win = True
            break
        # 直排
        elif(space[j]==space[j+3]==space[j+6]=="X"):
            print("玩家2獲勝")
            win = True   
            break
        elif(space[j]==space[j+3]==space[j+6]=="O"):
            print("玩家1獲勝")
            win = True      
            break             
    while not win:
        user1_input=int(input("玩家1請選擇要填入的位置"))
        if (0>user1_input or user1_input>8) or space[user1_input]=="X" or space[user1_input]=="O":
            print("所選位置已被選擇過或超出範圍")
            continue
        else:
            space[user1_input] = "O"
            while True:
                user2_input=int(input("玩家2請選擇要填入的位置"))
                if (0>user2_input or user2_input>8) or space[user2_input]=="X" or space[user2_input]=="O":
                    print("所選位置已被選擇過或超出範圍")
                    continue
                else:
                    space[user2_input] = "X"
                    break
            break

