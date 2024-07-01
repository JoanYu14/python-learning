# default argument一定要放在argument定義的最後面
def sayHi(word,name="noName"):
    print(f'{name}說:{word}')
sayHi(word="Hello") # noName說:Hello
