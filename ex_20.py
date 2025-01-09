#1
def greet(name):
    print(f"Hello,{name}!")
greet("World")

#2
def make_coffee(size):
    print(f"Making a coffee of {size}.")
    if size == "":
        return "defalt size"
make_coffee("")
#3
def introduce_myself(name,age,country="Japan"):
    print(f"My name is {name},I am {age} years old, and I am from {country}.")
introduce_myself("Mike",22)
#4
def sum_numbers(*ages):
    return sum(ages)
print(sum_numbers(1,2,3))
#5
def count_ares(*args):
    return len(args)
print(count_ares(*"Hello1"))
#6
def show_profile(**kwargs):
    for key,value in kwargs.items():
        print (f"{key},{value}")
profile = {"name":"Mike","age":22}
show_profile(**profile)    