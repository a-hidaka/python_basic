import requests

params = {
    "name": "mike",
    "age": 23
}
headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept": "text/html"
}
response = requests.get("https://httpbin.org/get", params=params, headers=headers)
print("Status code:",response.status_code)
print("Check url:",response.url)

print("--text--")
print(response.text)
print(type(response.text))
print("--json--")
print(response.json())
print(type(response.json()))

payload = {
    "name": "mike",
    "age": 23
}
response = requests.post("https://httpbin.org/post", data=payload)
print("Status code:",response.status_code)
print("Check url:",response.url)

print("--text--")
print(response.text)
print(type(response.text))
print("--post_json--")
print(response.json())
print(type(response.json()))

imgs = {
    "Accept": "image/png",
}

response = requests.get("https://httpbin.org/image", headers=imgs)
print(response.text)

with open("requests_text.png", "wb") as f:
    '''
    wb=>バイナリデータを読み取る
    '''
    f.write(response.content)

img = {
    "User-Agent":"Chrome",
    "Accept":"image/webp",
}
response = requests.get("https://httpbin.org/image", headers=img)
print(response.text)
with open("requests_test.webp","wb") as f:
    f.write(response.content)