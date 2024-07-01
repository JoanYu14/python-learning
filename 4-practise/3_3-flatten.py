# 寫一個名為「flatten」的函數來展平列表。
# flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]);
# # returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
def faltten(lst):
    falttened_lst = []
    # print(lst)
    # print(len(lst))
    for i in range(len(lst)):
        print(type(lst[i]))
        if type(lst[i]) != list:
            falttened_lst.append(i)
        else:
            print(type(lst[i]))
            for j in range(len(lst[i])):
                print(j)
    print(falttened_lst)
        # print(type(i))
        # for j in range(len(i)):
        #     print(j)
        #     print(type(j))
        # i_len = len(i)
        # print(f'element:{i}，len:{i_len}')

faltten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]])

