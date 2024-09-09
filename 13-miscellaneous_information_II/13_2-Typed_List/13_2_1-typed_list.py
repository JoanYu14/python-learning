# 自訂類型的 List，所有元素必須是相同的類型
class TypedList(list):
    def __init__(self, example_element, initial_list):
        """
        初始化方法，接受一個範例元素 example_element 用來確定列表中的元素類型，
        以及一個初始的列表 initial_list。
        """
        # 獲取 example_element 的類型，這將決定 TypedList 中所有元素的類型
        self.type = type(example_element)

        # 確認 initial_list 是一個 list
        if not isinstance(initial_list, list):
            raise TypeError("第二個參數必須是list")

        # 檢查 initial_list 中的每個元素，確保它們都與範例元素類型一致
        for element in initial_list:
            self.__check(self.type, element)

        # 複製 initial_list 中的元素，避免修改原列表
        self.elements = initial_list[:]  # 使用切片語法進行copy by value

        # 調用父類別的初始化方法，將 initial_list 傳入
        super().__init__(initial_list)

    def __check(self, list_type, element):
        """
        私有方法，用來檢查傳入的 element 是否與指定的 list_type 類型一致。
        如果類型不一致，則拋出 TypeError。
        """
        if type(element) != list_type:
            raise TypeError(f"{element}的型別必須是{list_type}，不能是{type(element)}")

    # __setitem__與__getitem__都可以不用定義會直接用list Class的__setitem__與__getitem__
    # def __setitem__(self, i, element):
    #     """
    #     覆蓋 __setitem__ 方法，確保當我們試圖修改列表中的元素時，
    #     新元素的類型必須與 TypedList 的指定類型一致。
    #     """
    #     # 檢查要插入的元素類型
    #     self.__check(self.type, element)
    #     # 調用父類別的 __setitem__ 方法進行設置
    #     super().__setitem__(i, element)

    # def __getitem__(self, i):
    #     """
    #     覆蓋 __getitem__ 方法，從列表中獲取指定索引處的元素。
    #     這裡是為了使其與標準列表行為保持一致。
    #     """
    #     # 調用父類別的 __getitem__ 方法
    #     return super().__getitem__(i)


# 測試程式碼
try:
    # 創建一個 TypedList，類型為 str，初始列表中的所有元素都是 str
    a = TypedList("123", ["123", "123", "1232"])
    print(a)  # 輸出：['123', '123', '1232']

    # 創建一個 TypedList，類型為 list，初始列表中所有元素都是 list
    # 注意第二個列表中有一個元素類型不一致（'4'是字符串，而其他是整數）
    b = TypedList(
        [1, 2, 3],  # 範例元素是 list
        [[1, 2, 3], ["4", 5, 6]],  # 這會拋出錯誤，因為元素類型不一致
    )
    print(b)  # 如果沒有錯誤，會輸出 [[1, 2, 3], ['4', 5, 6]]

    # 創建一個 TypedList，類型為 str，並且設置元素
    c = TypedList("", [""] * 5)
    c[2] = "13"  # 成功修改第 3 個元素為 "13"

    # c[3] = 12 會出現 TypeError，因為 12 不是 str 類型
    print(c)  # 輸出：['', '', '13', '', '']

    # 將兩個 TypedList a 和 c 進行相加，產生一個新的列表
    print(a + c)  # 輸出：['123', '123', '1232', '', '', '13', '', '']

    # 試圖創建一個類型為 str 的 TypedList，但其中包含一個整數，會拋出 TypeError
    b = TypedList("123", ["123", "345", 123])

# 捕獲基礎異常類型，並打印異常訊息
except BaseException as err:
    print(err)  # 輸出錯誤訊息，例如：123的型別必須是<class 'str'>，不能是<class 'int'>
