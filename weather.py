import requests
import pprint

endpoint = "https://weather.tsukumijima.net/api/forecast"


city_id = {
     "大阪府":270000,
     "京都府":260010
}

city = input("都市名を入力してください")
city = city_id[city]

params = {
 "city":city
     }


response = requests.get(endpoint,params=params)


dict_date = response.json()

pprint.pprint(dict_date)

print(f"日付:{dict_date['forecasts'][1]['date']}")
print(f"天気:{dict_date['forecasts'][1]['telop']}")
print(f"風:{dict_date['forecasts'][1]['detail']["wind"].strip("")}")
print(f"最低気温:{dict_date['forecasts'][2]['temperature']["min"]['celsius']}" + "℃")
print(f"最高気温:{dict_date['forecasts'][2]['temperature']["max"]['celsius']}" + "℃")


print(dict_date["forecasts"][1]["chanceOfRain"]["T00_06"].strip("%"))
print(dict_date["forecasts"][1]["chanceOfRain"]["T06_12"].strip("%"))
print(dict_date["forecasts"][1]["chanceOfRain"]["T12_18"].strip("%"))
print(dict_date["forecasts"][1]["chanceOfRain"]["T18_24"].strip("%"))

chanceOfRainOfkey = dict_date["forecasts"][1]["chanceOfRain"]
print("")
chanceOfRainList = {
    chanceOfRainOfkey["T00_06"],
    chanceOfRainOfkey["T06_12"],
    chanceOfRainOfkey["T12_18"],
    chanceOfRainOfkey["T18_24"],

}
print("降水確率をリストに格納し直した",chanceOfRainList)

chanceOfRainList = []
for date in chanceOfRainOfkey.value():
    print(date)
    chanceOfRainList.append(int(date.replace("%","")))

print("数字になったリスト",chanceOfRainList)

print((sum(chanceOfRainList)/len(chanceOfRainList)))