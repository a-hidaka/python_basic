from datetime import datetime
now = datetime.now()  #現在の日時取得
print(now)

#YYYY-MM-DD 形式で日付を取得
formatted_date = now.strftime("%Y-%m-%d")

#HH:MM:SS 形式で時間を取得
formatted_time = now.strftime("%H:%M:%S")

print(formatted_date)
print(formatted_time)

print("nowの型:",type(now))

from datetime import datetime,timedelta

#昨日の日時を取得
yesterday = now - timedelta(days=1)
#明日の日時を取得
tomorrow = now + timedelta(days=1)

print(yesterday)
print(tomorrow)

date1 = datetime(2022,1,1)
date2 = datetime(2022,2,1)
if date1 < date2:
    print("date1はdate2より昔です")

now = datetime.now()
if date1 < now:
    print("今の方が未来です")


import os
#現在のディレクトリの取得
current_dir = os.getcwd()
print(current_dir)

#ファイルサイズの取得
file_size = os.path.getsize("basic/basic_23.py")
print(file_size ,"バイト")

#ファイルがあるかないかの確認
exists = os.path.exists("basic_27.py")
print(exists)

if exists:
    print("Pythonの基礎は終了してそうです")
else:
    print("Pythonの基礎はまだ続きます")