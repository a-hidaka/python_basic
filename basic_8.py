''''basic_8.py'''
personal_date_list = ["Mike",20,"student","Osaka"]
personal_date_list[3] = "Wakayama"
print(personal_date_list)


num_list = list(range(1,10))
print(num_list)

multiple_of_two = list(range(2,20,2))
print(multiple_of_two)


my_list = [4,1,3,2]
sorted_list = sorted(my_list)
print(my_list)
print(sorted_list)

sorted_list = sorted(my_list,reverse=True)
print(sorted_list)


num1 = [1,2,3,4]
num2 = [10,20,30,40]
num1 += num2
num3 = num1 + num2
print(num1)
print(num3)

num1 = [1,2,3,4]
num2 = [10,20,30,40]
num3 = [num1,num2]
print(num3)


array = [1,12,2,50,1000,8]
max_value = max(array)
print("最大値→",max_value)


array = [1,12,2,50,1000,8]
min_value = min(array)
print("最小値→",min_value)


array2 = [1,2,3,4,5]
total_value = sum(array2)
print(total_value)
