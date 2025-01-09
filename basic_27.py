class Car:
    #属性（初期化）
    def __init__(self):
        print("必ず実行！")
    #メソッド
    def drive(self):
        print("ぶぅーーん")
my_car = Car()

class Car:
    #属性（初期化）
    def __init__ (self):
        self. color = "Green"
    #メソッド
    def drive(self):
        print(self.color+"の車が「ぶぅーーん」と走る")
my_car = Car ("Red")
print (my_car.color)

if __name__ == "__main__":
    my_car.color("Red")
    my_car.drive