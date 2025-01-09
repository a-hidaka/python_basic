class Animal:
   

    def __init__(self,name):
        self.name = name
        print("動物は鳴く")
    def speak(self):
        print("動物が音を出します。")
    

class Dog(Animal):
    pass

dog1 = Dog("ぼち")
print(dog1.name)

if __name__ == "__main__":
    dog = Dog("ぽち")
    dog.speak()

class Bird(Animal):
    def fly(self):
        print("空を飛んでます〜")

if __name__ == "__main__":
    dog = Dog("ぽち") 
    dog.speak()
    print("--------")
    bard = Bird("チュン太郎")
    bard.speak ()
    bard.fly()

class Animal:
    def __init__(self, name, life_span, intelligence):
        self.name = name
        self.life_span = life_span #寿命
        self.intelligence = intelligence #賢さ


class Dog (Animal):
    def __init__(self, name, life_span, intelligence):
        super().__init__(name, life_span, intelligence)
        self.name = "Dogクラス:" + name
        self.life_span = life_span
        self.intelligence = intelligence
        
if __name__ == "__main__":
    dog = Dog("ぽち","10年","かしこい")
    #dog.speak()
    print (dog.name )
    print (dog.life_span)
    print (dog.intelligence)
    # print ("------"）
    #bard=Bird（"チュン太郎"）
    # bard.speak()
    # bard.fly()

class Dog(Animal):
    def __init__(self, name, life_span, intelligence,cry):
        super().__init__(name, life_span, intelligence) 
        self.cry = cry

if __name__ == "__maim__":
    dog = Dog("ぽち","10年","賢い","わんわん")
    #dog.speak()
    print(dog.name)
    print(dog.life_span)
    print(dog.intelligence)
    print(dog.cry)