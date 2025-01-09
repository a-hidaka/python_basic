#1
list1 = [1,2,3,4,5,1,2,3,4,5]
list2 = set(list1)
print(type(list2))
#2
students = {'Alice','Bob','Charlie','David','Eve'}
students.remove('David')
print(students)
#3
math_students = {'Alice','Bob','Charlie'}
english_students = {'Bob','David','Eve'}
english_students2 = math_students.difference(english_students)
print(english_students2)
#4
math_english_student = math_students.intersection(english_students)
print(math_english_student)
#5
print(math_students.symmetric_difference(english_students))
#6
math_students.add('Frank')
print(math_students)
#7
last_year_users = {'Aさん','Bさん','Cさん'}
this_year_users = {'Aさん','Dさん',"Eさん"}
did_not_users = last_year_users.difference(this_year_users)
print(did_not_users)