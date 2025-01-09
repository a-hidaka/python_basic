#1
def hello():
    print("Hello!")
hello()
        

#2
def add_nunbers(a,b):
    return a + b
result = add_nunbers(3,5)
print(result)
#3
def get_length(text):
    return len(text)
result = get_length("Hello,World!")
print(result)
#4
def email_address_validation(email):
    if "@" in email:
        return True
    else:
        return False
result1 = email_address_validation("abcd@aaa.com")
result2 = email_address_validation("xyz.ne.jp")
print(f"文字1の場合→{result1}\n文字2の場合→{result2}")
#5
list1 = []
def list_genarate(start,end):
    list1 = [i for i in range(start,end)]
    return list1
result = list_genarate(1,6)
print(result)

