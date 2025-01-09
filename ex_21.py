#1
x = 10
def test():
    print("xの値は:",x)

test()
#2
x = 10
def test(x):
    #global x
    #x = 20
    print("xの値は:",x)
    return x
test(x)