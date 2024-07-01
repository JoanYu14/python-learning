# join
myList = ["a","b","c","d"]
myString = " & ".join(myList)
print(myString)

# sort, sorted
list1 = [1,3,2,6,5]
list2 = list1.sort() # sort return None
print(f"list1:{list1}\nlist2:{list2}") # list1被排序了
list3 = [2,8,4,7,5,1]
list4 = sorted(list3)
print(f"list3:{list3}  list4:{list4}") #list3:[2, 8, 4, 7, 5, 1]  list4:[1, 2, 4, 5, 7, 8]

# tuple sorted
tuple1 = (1,3,2,6,5)
# tuple1.sort() => AttributeError: 'tuple' object has no attribute 'sort'
sortedTuple1 = sorted(tuple1)
print(sortedTuple1) #[1, 2, 3, 5, 6]
print(type(sortedTuple1)) # <class 'list'>

# string sorted
word = "How are you"
print(sorted(word)) # [' ', ' ', 'H', 'a', 'e', 'o', 'o', 'r', 'u', 'w', 'y']

# in, notin
myList = ["a","b","c","d"]
print("a" in myList) # True
print("A" in myList) # False
print("a" in myString) # True
print("A" in myString) # False