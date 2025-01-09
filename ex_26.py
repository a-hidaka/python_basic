#1
with open("test1.txt",'w') as file:
    file.write("こんにちは！")
#2
with open("test1.txt",'r') as file:
    content = file.read()
    print(content)
#3
with open("test1.txt",'a') as file:
    file.write("今日は暑いですね")


