# String
for i in "Hello World":
    if(i==i.upper()):
        print(i) # H  W

# a list of tuple
for a,b in [(1,1),(2,3),(3,5),(4,6)]:
    print(a+b) # 2 5 8 10

# dictionary => 迭代key
dir = {"name":"Joan","age":23,"friends":["Isa","Jessica","metor"]}
for key in dir:
    print(f'dictionary的key:{key}，value:{dir[key]}')

for key,value in dir.items(): # .items將key與value變成一個個tuple
    print(f'dictionary的key:{key}，value:{dir[key]}')
# dictionary的key:name，value:Joan
# dictionary的key:age，value:23
# dictionary的key:friends，value:['Isa', 'Jessica', 'metor']


# set
for value in {1,3,5,6,7}:
    print(value)