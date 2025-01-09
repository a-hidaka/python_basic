count = 0
while count < 5:
    print(count)
    count += 1
print("whileの外")

user_input = ""
while user_input != "quit":
    user_input = input("「quit」を入力すると終了")
    print(user_input)

flag = True
count = 0
while flag:
    print(count)
    if count > 10:
        flag = False
    count += 1

cout = 0
while True:
    if count == 10:
        break
    print(count)
    count += 1

    fruits = ["apple","banana","orange"]
    index = 0
    while index < len(fruits):
        print(fruits[index])
        index += 1