import requests
import pprint

endpoint = "http://zipcloud.ibsnet.co.jp/api/search"

zipcode = input("郵便番号を入力してください。")

params = {
    "zipcode": zipcode
}

response = requests.get(endpoint,params=params)


dict_date = response.json()
pprint.pprint(dict_date)

print(dict_date['results'][0]['address1'])
print(dict_date['results'][0]['address2'])
print(dict_date['results'][0]['address3'])



