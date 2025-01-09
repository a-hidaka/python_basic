#1
fruits = ["apple","banana","grape"]
fruits.append("orange")
print(fruits)

#2
numbers = list(range(1,6))
numbers.insert(0,0)
print(numbers)
#3
colors = ["red","blue","green","yellow"]
print(colors.index("green"))
#4
languages = ["java","C","Python","Ruby"]
print(languages.index("Python"))
#5
shopping_list = ["apple","bsnana","orange","milk"]
removed_item = shopping_list.pop()
print(removed_item)
#6
names = ["Alice","Bob","Charlie","David"]
names.pop(2)
print(names)
#7
numbers = [5,2,8,1,9]
numbers.sort()
print(numbers)
#8
alphabets = ["c","a","b","f","d"]
alphabets.sort(reverse=True)
print(alphabets)
#9
original = ["one","two","three"]
copied = original.copy()
copied[0] = "Updated"
print(original)
print(copied)
#10
numbers = [1,3,5,2,5,4,5,5]
numbers.index(5)
print(numbers.count(5))
