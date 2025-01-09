
student = {"name":"Jhon",
           "age": 20,
           "grade": "A"}

keys = student.keys()
print(keys)

for key in student.keys:
    print(key)


Values = student.values()
print(Values)

for value in student.values():
    print(value)


numbers = {'a': 10,'b': 30,'c': 20}
max_key = max(numbers.values())
print(max_key)

items = student.items()
print(items)

for key,value in student.items():
    print(key,value)

 
student ={
    "name": "John",
    "age": 20,
    "grade": "A"}

#存在するキーの値の取得
name = student. get ("name")
print(name) #出力：John
#インデックスで値の取得
print (student ["name"]) # M#: John

#存在しないキーの値の取得
score = student.get ("score")
print (score) # #J: None
#インデックスで値の取得
#print (student ["score"]) # H7: KeyError: 'score'

if student.get("addrss"):
    print("addressは登録済みです")
else:
    print("adressの登録をしてください")

average_point = {"国語": 80,
"数学":
90,
"英語":
67}
english_average = average_point.pop("英語")
print(english_average)#出力：67
print(average_point) #出力：{"国語"：　80,"数学"： 90}

average_point = {
"国語": 80,
"数学": 90,
"英語": 67 }
science_average = average_point. pop("科学", 0)
print(science_average)#出力：0

student1 = {"name": "Mike",
"age": 20,
"from": "Osaka"}
student2 = student1.copy()
student2 ["name"] = "Nancy"
print (student1)
print(student2)

student3 = {"name": "Mike",
"age": 20,
"from": "Osaka"}
student4 = student3
student4 ["name"] = "Nancy"
print (student3)
print (student4)


 
