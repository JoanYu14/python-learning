print(__name__)  # __main__
if __name__ == "__main__":
    print("one.py是被直接執行，非在其他地方import")  # 直接執行會print此行
else:
    print("one.py是被import")  # 在其他地方被import會執行此行
