# 寫一個名為「palindrome」的函數來檢查輸入字串是否為回文。
def palindrome(words):

    # 創建名為 alphabetical_list 的新列表，其中包含以下元素：
    #   - x.upper()：對於列表 words 中每個符合條件的元素 x（即 x.isalpha() 為 True，表示 x 是一個字母(中文,韓文...也算)），
    #     使用 upper() 方法將 x 轉換為大寫字母形式。
    #   - for x in words：遍歷列表 words 中的每個元素 x。
    #   - if x.isalpha()：條件過濾，只有當元素 x 是一個字母（即 x.isalpha() 為 True）時，才將 x 放入 alphabetical_list 中。
    alphabetical_list = [x.upper() for x in words if x.isalpha()]

    # Python不能像JS直接把.function()回傳的值直接傳給.function()，所以一定要分開
    # 在 JavaScript 中，對象的方法可以直接鏈式調用，每個方法返回的是該對象本身或者另一個新對象。
    # reversed_alphabetical_list = alphabetical_list.copy().reverse() 
    reversed_alphabetical_list = alphabetical_list.copy()
    reversed_alphabetical_list.reverse() # 這會直接更改list，return None，也就是說他是直接去那個記憶體位置更改list了
    print(f"原始list:{alphabetical_list}")
    print(f"反轉list:{reversed_alphabetical_list}")
    return alphabetical_list==reversed_alphabetical_list

def palindrome2(words):
    alphabetical_list = [x.upper() for x in words if x.isalpha()]
    for i in range(len(alphabetical_list)//2):
        if alphabetical_list[i]==(alphabetical_list[-1-i]):
            print(f'index{i}:{alphabetical_list[i]}與index{-1-i}:{alphabetical_list[-1-i]}相同')
        else:
            return False
    return True

input_words = input("請輸入字串:")
print(f'{input_words}是否為回文:{palindrome(input_words)}')
print(f'{input_words}是否為回文:{palindrome2(input_words)}(2)')