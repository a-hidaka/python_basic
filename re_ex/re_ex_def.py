import re
#1
def Hello():
    print("Hello!!")
Hello()
print("-------")
#2
def add_numbers(a,b):
    return a + b
result = add_numbers(3,5)
print(result)
print("-------")
#3
def get_length(text):
    return len(text)
result = get_length("Hello,World!!")
print(result)
print("-------")
#4
def email_address_validation(text):
    if "@" in text:
        return True
    else:
        return False
a = email_address_validation("absd@aaa")
b = email_address_validation("xyz.ne.jp")
print(a,b,sep="\n")
def email2_address_validation(text):
    if re.match('[a-z]+[0-9]?\@\w\.[a-z.]+',text):

        return True
    else:
        return False
c = email2_address_validation("absd@aaa")
d = email2_address_validation("xyz.ne.jp")
print(c,d,sep="\n")
print("------")
#5
def list_generate(start,end):
    list1 = []
    for i in range(start,end):
        list1.append(i)
    return list1
result = list_generate(1,6)
print(result)