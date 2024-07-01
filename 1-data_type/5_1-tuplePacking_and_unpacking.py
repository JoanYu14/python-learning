# Tuple打包意味著Python會自動將用逗號","分隔的資料打包到一個Tuple中
a = 10,15 # 自動打包成tuple (10,15)
print(a) # (10, 15)
print(type(a)) # <class 'tuple'>

# Tuple解包意味著將Tuple的各個元素（以逗號","分隔）分配給多個變數。
# 將a[0]給a1, a[1]給a2
a1,a2 = a
print(f"a1={a1}, a2={a2}") # a1=10, a2=15

# 對調
x=25
y=35
print(f"x={x},y={y}")
# 右邊y,x會先自動打包成一個tuple(x,y)=>(35,25)，左邊對右邊tuple做unpacking依序賦值給x,y變數，所以就對調了
x,y=y,x 
print(f"x={x},y={y}")
