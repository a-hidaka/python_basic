import requests
import pprint
import datetime

end_point = "https://weather.tsukumijima.net/api/forecast"

city_dict = {
    "osaka":270000
}

param = {
    "city":city_dict["osaka"]
}

response = requests.get(end_point,params=param)

dict_date = response.json()

pprint.pprint(dict_date)

print(f"日付:{dict_date['forecasts'][1]['date']}")
print(f"天気:{dict_date['forecasts'][1]['telop']}")
print(f"風:{dict_date['forecasts'][1]['detail']["wind"].rstrip("")}")
print(f"最低気温:{dict_date['forecasts'][2]['temperature']["min"]['celsius']}" + "℃")
print(f"最高気温:{dict_date['forecasts'][2]['temperature']["max"]['celsius']}" + "℃")



chanceOfRainOfkey = dict_date["forecasts"][1]["chanceOfRain"]
print("")
chanceOfRainList = {
    chanceOfRainOfkey["T00_06"],
    chanceOfRainOfkey["T06_12"],
    chanceOfRainOfkey["T12_18"],
    chanceOfRainOfkey["T18_24"],
}


chanceOfRainList = []
for date in chanceOfRainOfkey.values():
    (date)
    chanceOfRainList.append(int(date.replace("%","")))



print("降水確率(平均値):",(sum(chanceOfRainList)/len(chanceOfRainList)),"%",sep="")

dt4 = datetime.datetime.today() + datetime.timedelta(days=1)
strd4 = dt4.strftime('%Y年%m月%d日')

rainchance = sum(chanceOfRainList)/len(chanceOfRainList)

message = "明日:" + strd4 + "の天気"+ "\n天気:" + dict_date['forecasts'][1]['telop'] + "\n風:" + dict_date['forecasts'][1]['detail']["wind"].rstrip("") + "\n最低気温:" + dict_date['forecasts'][2]['temperature']["min"]['celsius'] + "℃" + "\n最高気温:" + dict_date['forecasts'][2]['temperature']["max"]['celsius'] + "℃" + "\n降水確率(平均値):" + str(rainchance) + "%"
    
#VPfMDUmR43ZC8FWAjOYMRiitzTzJBf82EZNJHCarPry
