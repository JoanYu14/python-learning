counter = 0
row1 = [' ', ' ', ' ']  # 第一行的初始狀態
row2 = [' ', ' ', ' ']  # 第二行的初始狀態
row3 = [' ', ' ', ' ']  # 第三行的初始狀態


def display(row1, row2, row3):
    """顯示目前遊戲盤面"""
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    """讓玩家輸入位置"""
    choice = input("請輸入一個數字 (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("抱歉，您的輸入不是數字")
        else:
            print("您的選擇不在 1 - 9 的範圍內。")
        choice = input("請輸入一個數字 (1-9): ")
    return int(choice)


def getCurrentSymbol():
    """取得當前玩家的符號（X 或 O）"""
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list[counter % 2]


def update_table(index):
    """更新遊戲盤面"""
    global row1, row2, row3
    if index in range(1, 4):  # 如果是1到3的位置，更新第一行
        if row1[index - 1] == ' ':
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):  # 如果是4到6的位置，更新第二行
        if row2[index % 3 - 1] == ' ':
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    else:  # 如果是7到9的位置，更新第三行
        if row3[index % 3 - 1] == ' ':
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False


def check_winning():
    """檢查是否有玩家獲勝"""
    player_1_wins = False
    player_2_wins = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):  # 檢查第一行是否有三個連線
        if (row1[0] == "X"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):  # 檢查第二行是否有三個連線
        if (row2[0] == "X"):
            player_2_wins = True
        elif (row2[0] == "O"):
            player_1_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):  # 檢查第三行是否有三個連線
        if (row3[0] == "X"):
            player_2_wins = True
        elif (row3[0] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):  # 檢查第一列是否有三個連線
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):  # 檢查第二列是否有三個連線
        if (row1[1] == "X"):
            player_2_wins = True
        elif (row1[1] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):  # 檢查第三列是否有三個連線
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[1] != " " and row3[2] != " ")):  # 檢查左上到右下的對角線是否有三個連線
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):  # 檢查右上到左下的對角線是否有三個連線
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True

    if player_1_wins:
        return "player 1 wins"
    elif player_2_wins:
        return "player 2 wins"
    else:
        return "no one wins"


def start_game():
    """開始遊戲"""
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("錯誤的位置，請重新選擇")

        result = check_winning()
        if result == "player 1 wins":
            display(row1, row2, row3)
            print("玩家 1 獲勝!! 恭喜恭喜")
            return
        elif result == "player 2 wins":
            display(row1, row2, row3)
            print("玩家 2 獲勝!! 恭喜恭喜")
            return
        elif result == "no one wins" and counter == 9:
            display(row1, row2, row3)
            print("平局!!")
            return


start_game()
