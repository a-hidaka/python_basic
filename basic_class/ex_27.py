#1,2,3,4,
class User:

    def __init__(self,name,age) :
       self.name = name
       self.age = age
    def get_name(self):
       print(self.name)
    def get_age(self):
       print(self.age) 

my_user = User("山田",22)
print(my_user.name)
print(my_user.age)
my_user.get_name()
my_user.get_age ()  
