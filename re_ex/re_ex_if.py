number_list = [1, 2, 3, 4, 5, 6]
for i in number_list:
    if i % 2 == 0 and i % 3 == 0:
        print("2と3の公倍数です")
    elif i % 2 == 0 :
        print("2の倍数です")
    elif i % 3 == 0 :
        print("3の倍数です")
    else:
        print("それ以外です")