#1
fruits = ["apple","banana","grape"]

for i in fruits:
    print(i)
#2
numbers = [1,2,3,4,5]

for i in numbers:
    print(i,end="")
#3
print()
for i in range(1,11):
    print(i,end="")
#4
print()
for i in range(1,6,+2):
    print(i)
#5
shopping_list = ["apple","banana","orange","milk"]
number = [1,2,3,4,5]

for i,a in zip(shopping_list,number):
    print(f"{a}番に{i}を買います")
#6
names = ["Alice","Bob","David"]

for i in names[:3]:
    print(i)
else:
    print("以上です。")
#7
numbers = [1,2,3,4,5]

for i in range(6,11):
    numbers.append(i)
print(numbers)
#8
double_numbers = []
numbers = [1,2,3,4,5]

for i in numbers:
    double_numbers.append(i*2)
print(double_numbers)
#9
lower_char_list = ["a","b","c"]
upper_char_list = ["A","B","C"]

for lower,upper in zip(lower_char_list,upper_char_list):
    print(lower+upper)
#10
lower_char_list = ["a","b","c"]
upper_char_list = ["A","B","C"]

for i in range(3):
    print(lower_char_list[i],upper_char_list[i],sep="")
   


