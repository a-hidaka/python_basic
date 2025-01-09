#1
student_id_number = [2101,2102,2103,2104]
print(student_id_number)
#2
weather_today = "今日はいい天気ですね！"
print(list(weather_today))
#3
print(weather_today[5])
#4
print(student_id_number[-1])
#5
club_activities = [["Mike","baseball"],["Nancy","soccer"],["John","music"],["Tom","science"]]
print(club_activities[3][1])
#6
print(club_activities[2][0])
#7
print(f"わたくし{club_activities[0][0]}は、{club_activities[0][1]}部に所属しています！")
#8,9
number_list = [1,2,3,4,5,6,7,8,9]
d = [number_list[0:3]]
print(d)
number_list.reverse()
print(number_list)
#10
number_list.reverse()
number_list2 = []
a = 0
b = 3
for i in range(3):
     c = number_list[a:b]
     number_list2.append(c)
     a += 2
     b += 2
a = [1,2,3]
b = [10,20,30]
c = [a , b]
print(c)
#print(number_list2)
#11
x = [[1,2,3],[4,5,6],[7,8,9]]
print(x[0][0])
#12
print(x[1][1])
#13
print(x[2][2])

