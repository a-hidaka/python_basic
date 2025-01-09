person = {
    "name": "Jhon",
    "age": 25,
    "city":"Tokyo"}

print(type(person))
print(person["name"])
print(person["age"])
print(person["city"])

person = {"name": "Alice", "age": 25, "city": "Tokyo"}
print (person ["name" ] )
#出力：Alice
print (person ["age"])
#出力：25
person ["city"] = "Osaka"
print (person ["city"])

person = {"name": "Alice", "age": 25, "city": "Tokyo"}
person ["birthplace"] = "Tokyo"
print (person)

person = {"name": "Alice", "age": 25, "city": "Tokyo"}
person ["birthplace"] = "Tokyo"
print (person) 
del person ["city"]
print (person)


empty_dict = 1
print (empty_dict)
#↑出力：｛｝
print (type (empty_dict))
#个出力：<class'dict'>

person = {
"name": "Alice",
"age": 25,
"city": "Tokyo"}
print(len(person))#出力：3

#ネストした辞書型の例
student = {
"name": "John",
"age": 20,
"grades":{
"math":80,
"english": 75,
"science": 90}}
#ネストした辞書型の値にアクセス print (student ["name"]) # Щ: John
print(student ["grades"] ["math"]) # H #: 80

#辞書のソート例
scores = {
"math": 80,
"english": 75,
"science": 90}
#辞書をキーでソート
sorted_keys = sorted (scores)
#ソートされたキーに基づいて値にアクセス
for key in sorted_keys:
 print(key, scores [key])


dic = {"A": "cat", "B": "dog"}
print(dic.setdefault("C", "hoge"))
# 出力
# "hoge"
# 第一引数に参照したいkeyを入れる
# keyがなかった場合、第二引数の値を返す

# setdefault()で追加された要素は、元の辞書に反映される
print(dic)

lst = ["A", "B", "C", "D", "E"]
dic = {}
n = 1
for i in lst:
    # nが奇数が偶数かでkeyを振り分ける
    # setdefault()の第二引数は空リスト=[]にしておく
    if n % 2 == 1:
        dic.setdefault(1, []).append(i)
    elif n % 3 ==1:
       dic.setdefault(2,[]).append(i)
    else:
        dic.setdefault(3, []).append(i)
    n += 1
print(dic)

number = {
   "a": 10,
   "b": 30,
   "c":20
}

max_number = number.values()
print(max_number)