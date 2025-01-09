#1
print("こんにちは、{}さん".format("山田"))
#2
print("こんにちは、{}。{}さんが呼んでいましたよ。".format("武田","山田"))
#3
a = "abcd@co.jp"
b = a.replace("@","アットマーク")
print(b)
#4
x = "abcd@xyz@co.jp"
y = x.replace("@","アットマーク",1)
print(y)
#5
name = "山田"
print(f"{name}さん、こんにちは！！")
#6
word = "あしたははれですか？"
print(word.count("は"))
#7
str_number = "123456789"
print(str_number.find('6'))
#8
greeting = "Hi,Myname is John"
print(greeting.upper())
#9
print("NANCY".lower())
p = "mike**jj" 
print(p.replace("**",""))
