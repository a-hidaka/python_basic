'''basic_11.py'''

for char_text in "abcdef":
    print(char_text)
    print("for-end")

numbers = [10,20,30]
for number in numbers:
    print(numbers)

numbers2 = [1,2,3,4,5]
for i in range(2,len(numbers2)):
    print(numbers2[i])

numbers = [1,2,3,4,5]
double_numbers = []

for number in numbers:
    double_numbers.append(number*2)
print(double_numbers)

runnner_list = ["Aさん","Bさん","Cさん"]
for index,person in enumerate(runnner_list):
    print(f"インデックス番号{index}番は{person}です。")

posts = ["部長","課長","係長"]
names = ["Aさん","Bさん","Cさん"]

for name,post in zip(names,posts):
    print(f"{name}は{post}です。")
else:
    print("ループ終了")