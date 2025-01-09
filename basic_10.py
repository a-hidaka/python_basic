'''
basic_10.py
・ミュータブルとイミュータブル
・タプル
'''
my_tuple  = ("Mike",20,"student","Osaka")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
#my_tuple[0] = "Tom"
my_tuple2 = 1,2,3
print(my_tuple2)
base_list = [1,2,3]
make_tuple = tuple(base_list)
print(make_tuple)

change_to_list = list(make_tuple)
print(change_to_list)