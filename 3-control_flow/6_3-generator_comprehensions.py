# 生成器推導式
# (表達式 for 元素 in 可迭代對象 if 條件)
# 基本語法與列表list推導式類似，只是將方括號 [] 替換為圓括號 ()

# 生成平方數生成器
squares_gen = (x**2 for x in range(10))

print(squares_gen) # <generator object <genexpr> at 0x0000027CC65C9510>

# 遍歷生成器
for square in squares_gen:
    print(square)  # 依次輸出 0, 1, 4, 9, 16, 25, 36, 49, 64, 81