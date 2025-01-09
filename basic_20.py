def greet (name="山田さん"):
    print(f"こんにちは{name}さん")
greet()
greet("田中さん")


def add_number(*args):
    print(args)    
    return sum(args)
result1 = add_number(1,2,3,4,5)
print(result1)
numbers = {
    "name":"Mike"
}
result3 = add_number(*numbers)

def print_student_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_student_info(name="Mike") 

student_infomation = {
    "name":"Jihn",
    "age":22
}
    

    