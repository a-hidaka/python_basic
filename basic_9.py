personal_date_list = ["Mike",20,"student","Osaka"]
personal_date_list.append("soccer")
print(personal_date_list)

foods = ["たこ焼き","お好み焼き","串かつ","どて焼き","かすうどん"]
foods.insert(2,"焼きそば")
print(foods)

print(foods[-1])


country_list = ["America","India","Italy","Japan"]
print(country_list.index("Japan"))
#print(country_list.index("Korea"))


homework_list = ["国語","数学","英語"]
homework_list.pop()
print(homework_list)

homework_list.pop(1)
print(homework_list)

del_word = homework_list.pop()
print(homework_list,del_word,sep="戻り値は、")

num_list = [3,10,2,1,]
num_list.sort(reverse=True)
print(num_list)


list1 = [1,2,3,4,5]
list2 = list1
print(list1,list2)
list2[0] = 100
print(list1,list2)
c_list = [1,2,3]
c_list2 = c_list.copy()
c_list2[0] = 100
print(c_list,c_list2)