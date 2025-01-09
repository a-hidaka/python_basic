class Member:

    def __init__(self,student_number,name,grade,age):
        self.student_number = student_number
        self.name = name
        self.age = age
        self.grade = grade

    def self_introduction(self):
        print(self.name + "は" + self.grade + "年生" + self.age + "歳です")
    #インスタンス化(自分の情報をゲット)
    #student_number(属性)をprint()表示
    #インスタンス化からself_introductionを実行して、戻り値をprint()で表示
me = Member("2405911","日髙燿","1","21")
print(me.student_number)
me.self_introduction()

