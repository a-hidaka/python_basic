from datetime import date,datetime,timedelta,timezone


today = date.today()
weekdays = ["月曜日","火曜日","水曜日","木曜日","金曜日","土曜日","日曜日"]
print(today)
print(today.year)
print(today.month)
print(weekdays[today.weekday()])
print(today.day)
print(type(today))
print("-----------")

target_date = date(2024,12,5)
print(target_date)
print(target_date.weekday())
print(type(target_date))
print("------------")

now = datetime.now()
print(now)
print(now.year) #年
print(now.month) #月
print(now.day) #日
print(now.hour) #時間
print(now.minute) #分
print(now.second) # 秒
print(now.microsecond) #マイクロ秒
print("------------")

my_birthday = datetime(2003,5,2)
print(my_birthday)
print("------------")

now = datetime.now()
print(now - my_birthday)
print(type(now - my_birthday))
diff = now - my_birthday
print(diff.days,"日")
print(diff.days*24,"時間")
print(diff.seconds/(60*60))
print(diff.seconds*60,"分")
print(diff.seconds)
print(diff.microseconds)
print("------------")

date_01 = datetime(2023, 12, 31, 3, 0, 0, 0)
result = date_01 + timedelta(days=1)
print(result)
print("------------")

jst = timezone(timedelta(hours=+9))
result01 = datetime.now(jst)
result02 = datetime(2023, 12, 31, 0, 0, 0, 0, jst)
print(result01)
print(result01.tzinfo)
print(result02)
print(result02.tzinfo)
print("------------")

# 2つの日付を作成
date1 = datetime(2024, 1, 1)  # 2024年1月1日
date2 = datetime(2024, 2, 1)  # 2024年2月1日
# 等しいか比較 (==)
print(date1 == date2)  # False
# より大きい (>)
print(date2 > date1)   # True（date2の方が未来なので）
# より小さい (<)
print(date1 < date2)   # True（date1の方が過去なので）
# 以上、以下 (>=, <=)
print(date1 <= date2)  # True
print(date2 >= date1)  # True
print("------------")

# 現在の日時を取得
now = datetime.now()
# 期限日の設定
deadline = datetime(2024, 12, 31)  # 2024年12月31日
# 期限切れかどうかをチェック
if now > deadline:
    print("期限が過ぎています")
else:
    print("まだ期限内です")
# 残り日数を計算
days_left = (deadline - now).days
print(f"残り{days_left}日")

print("#1")
seven_days = now + timedelta(days=+7)
print(seven_days.strftime('%Y年%m月%d日 (%a)'))
print("#2")
date1 = datetime(2024,12,25,15,30,00)
weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
print(weekdays[date1.weekday()])
print("#3")
date2 = now + timedelta(hours=+1.5)
print(date2.strftime('%H時%M分'))
print("#4")
date1 = date(2024,12,31)
date2 = date(2025,1,1)
result = date2 - date1
print(result.days,"日")
print('#5')
u_birthday = date(2024,12,25)
today = date.today()
result01 = u_birthday - today
print(f"誕生日まで{result01.days}日")