import random

hands = ["グー","チョキ","パー"]

while True:
  try:
    user_hands = int(input("数字を入れてください\nグー(0),チョキ(1),パー(2):"))
    if user_hands < 0 or user_hands > 2:
        raise ValueError
    break
  except ValueError:
    print("0〜2の整数を入力してください")
  

computer_hand = random.randint(0,2)
cnt = 0                

while True:
 print("継続中" + cnt)
 cnt += 1 
 if cnt >= 10:
  break
 print(f"あなた{hands[user_hands]},コンピューター:{hands[computer_hand]}")

 if user_hands == computer_hand: 
  print("あいこ")
 elif (user_hands - computer_hand + 3) % 3 == 1:
  print("負け!!!")
 else:
  print("勝ち!!!")