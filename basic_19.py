def say_hello():
    print("Hello World!")

say_hello()


def greet(name):
    print("Hello",name)

name1 = "Mike"
name2 = "Nancy"

greet(name1)
greet(name2)


def sekf_introduction(firstName, lastName):
    print(f"私は{firstName} {lastName}です")
firstName = "Shibaike"
lastName = "Kengo"

sekf_introduction(firstName,lastName)


x = 10
y = 100

def add(x,y):
    print(x + y)
x = 1
y = 2
add(x,y)


def age_confirmation(age):
    if age >= 20:
        return "成人"
    else:
        return "ガキ"
result = age_confirmation(22)
print(result)