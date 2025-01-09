"""basic_6.py(メソッド)"""
good_morning = "みなさん、おはようございます。"
good_evening = good_morning.replace("おはようございます","こんばんは")
print(good_evening)

print("{}、こんにちは".format("田中さん"))
friend = "田中さん"
print("{}、こんにちは".format(friend))
print("{0}、こんにちは。{0}は{1}歳ですよね？".format("田中さん",30))
print("{name}さん、こんにちは".format(name="角田"))
name = "Mike"
print(f"{name}は早起きです")

string = "hi hi hi python!!"
print(string.translate(str.maketrans("hi", "HI", "!!")))

x = "abcd@xyz@co.jp"
print(x.replace(x[8:9],"アットマーク"))
print(x.index("@",5))