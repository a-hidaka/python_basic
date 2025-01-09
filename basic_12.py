

if True:
    print("Trueやから実行される")

if False:
    print("Trueやから実行される")
print("if文おわってるよ")

is_registered = True
if is_registered:
    print("登録済みです")

greeting = ""
if greeting:
    print(greeting)

    greeting = "こんにちは"
if greeting:
    print(greeting)

x = 10
y = 30
if y > x:
    print("yはxより大きです")

if y > x and y <= 200:
    print("どっちもTrueです")


is_empty = False

if not is_empty:
    print("Trueになる")

members = ["AAA", "BBB", "CCC"]
entry_comfirm = "AAA"
if entry_comfirm in members:
    print(f"{entry_comfirm}は登録済みです")

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number == 5:
        break
    print(number)


numbers = [1,2,3,4,5,6,7,8,9,14]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number == 9:
        break
    if number % 2 == 0:
        continue
    print(number)