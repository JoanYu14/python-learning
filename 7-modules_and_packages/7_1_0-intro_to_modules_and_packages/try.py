# 從another_module導入one_function與two_function函數
# 在執行這行程式碼時，python會去another_module.py裡面將這兩個函數轉成byte codes，也就是電腦可以直接執行的東西
from another_module import one_funtion,two_function
one_funtion() # Hello from another_module.py.
two_function() # this is two_function from another_module.py.