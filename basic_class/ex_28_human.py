#1
class Human:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def introduce(self):
        print(f"{self.name}は{self.age}歳です。")
   
#2
class Student(Human):
    def introduce(self):
        print("私は学生です")
#3
class Teather(Human):
    def introduce(self):
        print("私は教師です")
#4
a = Human("太郎",25)
b = Student("花子",20)
c = Teather("佐藤",35)
a.introduce()
b.introduce()
c.introduce()