import datetime
class Shop:
    def __init__(self, name, holiday, business_hours, tel):
        self.name = name
        self.holiday = holiday
        self.business_hours = business_hours
        self.tel = tel

weekday = datetime.datetime.now().strftime('%A')
weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
today_weekday = weekdays[datetime.datetime.today().weekday()]

main_store = Shop("本店", weekday[3], "10:00~21:00", "0120-000-0000")