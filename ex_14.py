#1
product = {
    "id": "P001",
    "name": "iPhon 12",
    "price": 99900,
    "brand": "Apple"}
print(product["brand"])

print(len(product))

vantan = {
    "月曜日": "デザインシンキング",
    "火曜日": "Python",
    "水曜日": "Webデザイン"}
print(vantan)

population = {
    "Tokyo": 12929286,
    "Osaka": 8839469,
    "Nagoya": 2378140,
    "Fukuok": 1559971}
population["Osaka"] = 200
print(population["Osaka"])

del population["Fukuok"]
print(population)

students = {
    "student1": {"name": "Alice", "age": 18, "grade": "A"},
    "studdent2": {"name": "Bob", "age": 17, "grade": "B"},
    "student3":{"name": "Charie","age": 16, "grade": "C"}}
print(f"{students['studdent2']["name"]}の年齢は{students['student3']["age"]}歳です。")
word = {
    "b": "びー","c": "しー","a": "えー"} 

r_word = sorted(word)
for i in r_word:
    print(word[i])

#2
#3
#4
#5
#6
#7

