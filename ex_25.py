#1
try:
    name = "Nancy"
    age = 32
    print(name + "は" + age + "天才です。")
except TypeError:
    print("エラーが出たみたい")
#2
try:
    name = "Nancy"
    age = 32
    print(name + "は" + age + "天才です。")
except TypeError as a :
    print("エラーが出たみたい",a)