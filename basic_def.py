#number = int(input())
#input_number = input("好きな数字を入力してください:")
#def odd_or_even(number):
    #if number % 2 == 0:
        #return "偶数です"
    #else:
        #return "奇数です"



##result = odd_or_even(input_number)
#print(result)

# def lottery(value):
#     if value == "偶数です":
#         print("大吉")
#     else:
#         print("大凶")

# #lottery(result)

# id = 9999
# password = "kkkk"

# input_id = input("idを入力してください:")
# input_password = input("パスワード入力してください:")

# def login(input_id,input_password):
#     if id == input_id and password == input_password:
#         return "合格"
#     elif id == input_id and password != input_password:
#         return "不合格"
#     elif id != input_id and password == input_password:
#         return "不合格"
#     else:
#         return "ざこ"
# login(input_id,input_password)

amount = int(input("数字>"))
in_or_out = input("イートインorテイクアウト>")

def add_tax(amount):
    if in_or_out == "イートイン":
        return amount * 1.1
    elif in_or_out == "テイクアウト":
       return amount * 1.08
    else:
       
       print("イートインかテイクアウトか選べ")

result = add_tax(amount)
print(result)

input_pay = int(input("いくら払いますか？>"))


def paypay(result):
    if result == input_pay:
        print("ちょうどです")
    elif result > input_pay:
        print("お金が足りません")
    else:
        print("お釣りは",input_pay - result,"円です",sep="")
paypay(result)

    


       





