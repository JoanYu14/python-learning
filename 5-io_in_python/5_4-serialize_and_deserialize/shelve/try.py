import shelve

integers1 = [1,2,3,4,5,6]
integers2 = [7,8,9,10]
integers3 = [95,96,97,98,99,100]

# flag = c是創建的意思
with shelve.open("my_shelve_file",flag="c") as shelf:
    # shelf是dictionary的形式儲存的
    shelf["ints1"] = integers1
    shelf["ints2"] = integers2
    shelf["ints3"] = integers3    

with shelve.open("my_shelve_file",flag="r") as shelf:
    for key in shelf.keys():
        print(f"key={key}，value={shelf[key]}")
        # key=ints1，value=[1, 2, 3, 4, 5, 6]
        # key=ints2，value=[7, 8, 9, 10]
        # key=ints3，value=[95, 96, 97, 98, 99, 100]
