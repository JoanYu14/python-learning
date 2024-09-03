def new_decorator(original_func):
    def wrap_func():
        print("Here is some code before the original function")
        original_func()
        print("Here is some code after the original function")

    return wrap_func


def func_needs_decorator():
    print("I'm a function that needs decorator")


decorator_function = new_decorator(func_needs_decorator)
decorator_function()
# Here is some code before the original function
# I'm a function that needs decorator
# Here is some code after the original function


# 使用decorator(裝飾器)
# 裝飾器的語法，使python知道use_decorator_func實際上是被放入new_decorator的參數中使用
# 而我們呼叫use_decorator_func就是將use_decorator_func放入new_decorator參數中並呼叫
@new_decorator
def use_decorator_func():
    print("I am a function that uses decorators.")


use_decorator_func()
# Here is some code before the original function
# I am a function that uses decorators.
# Here is some code after the original function

# 我們在6_4在Class內有使用到@propety，這個是python幫我們內建的裝飾器
# 主要用來將類別中的方法轉換為屬性，使得方法可以像屬性一樣被訪問，而無需顯式調用。
# 使用 @property 的好處
# 控制屬性訪問：你可以在屬性被訪問或設置時添加邏輯，比如驗證數據或觸發其他操作。
# 避免接口變更：如果你開始時使用了屬性，後來需要在訪問時執行一些邏輯，@property 可以讓你在不改變類別外部接口的情況下進行修改。
# 簡化接口：使用 @property 可以使你的類別接口更加簡單和直觀，因為用戶可以通過簡單的屬性訪問而非方法調用來獲取值。
