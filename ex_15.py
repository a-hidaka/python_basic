#1
person = {
    'nsme':"Alice",
    'age': 25,
    'city': 'Tokyo'
}
for key,value in person.items():
    print(key,value)





#2
student_scores = {
    "Mike": 85,
    "Emily": 92,
    "John": 78,
    "Sarah": 95
}
student_scores2 = student_scores.pop("Mike")
print(student_scores)
#3
products = {
    "orsnge": 20,
    "apple": 32,
    "banana": 9
}

if "apple" in products:
    print(f"{products['apple']}個あります")
else:
    print("ありません")
#4
product_prices = {
    "apple": 100,
    "banana": 180,
    "orenge": 200,
    "grape": 600
}
for value in product_prices.values():
    print(value)
#5
for key,value in student_scores.items():
    print(f"{key}さんは{value}点でした")
#6
students = {
    "Alice": {
        "age": 20,
        "natinality": "USA"
    },
    "Bob": {
        "age": 22,
        "nationality": "Uk"     
    },
    "Catharine": {
        "age": 19,
        "nationality": "Canada"
    }
}
print(students["Bob"]["age"])
#7
for key in students.keys():
    if students[key]["age"] >= 20:
        print(key)
#for key,value in students.items():
    #if students[key]["age"] >= 20:
        #print(key)