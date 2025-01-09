#1
x = -1

if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロ")
#2
x = 0

if x > 0:
    print("正の数です")
elif x < 0:
    print("負に数です")
else:
    print("ゼロ")
#3
x = 6

if x > 0:
    print("正の数です")
elif x < 0:
    print("負の数です")
else:
    print("ゼロ")
#4
y = 50

if y >= 0 and 100 >= y:
    print("範囲内です")
else:
    print("範囲外です")
#5
y = 200

if y >= 0 and 100 >= y:
    print("範囲内です")
else:
    print("範囲外です")
#6
shopping_list = ["apple","cake","carrot","water"]

for i in range(len(shopping_list)):
    if shopping_list[i] == "apple":
        print("フルーツです")
    elif shopping_list[i] == "carrot":
        print("野菜です")
    else:
        print("不明です") 
#7
number_list = [1,2,3,4,5,6]

for i in number_list:
    
    if i % 2 == 0 or i % 3 == 0:

        if i % 2 == 0 and i % 3 != 0:
            print("2の倍数です")
        elif i % 2 != 0 and i % 3 == 0:
            print("3の倍数です")
        else:
            print("2と3の公倍数です")
    else: 
        print("それ以外です")