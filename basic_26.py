file = open ("file.txt", "w")
file.write("Hello, World!")
file. close ()

file = open("file.txt",
'w')
text = """\
あああああ
いいいいい
ううううう
えええええ
おおおおお
"""

file.write (text)
file. close ()

with open("filel.txt", "w") as file:
    file.write("書き込みます。")

with open("filel.txt", "r") as file:
    #ファイルの内容を読み取る
    content = file. read ()
    print ( content)

with open("filel.txt","a")as file:
    #ファイルの内容を読み取る
    file.write("書き足します！\n")