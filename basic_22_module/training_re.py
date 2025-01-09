import re

m = re.match('a.c','abc')
print(m)
print(m.group())
m1 = re.match('an','ananan')
print(m1)
m2 = re.match('ab*','abcbbbb')
m3 = re.match('ab?123','abffff123')
print(m2,m3)

m7=re.match('abc?123', 'ab123')
print(m7)
m4 = re.match('ab+c','abbbbdc')
print(m4)
m5 = re.match('ab{2}','abbbb')
print(m5)
m6 = re.match('[a-c]','b')
m7 = re.match('[a-c]','f')
m8 = re.match('[0-9]','09012345678')
m9 = re.match('[0-9０-９]*','００００８０１２３')
print("<m6〜m9>",m6,m7,m8,m9,sep="\n")
m10 = re.match('[^\w]','ac')
m11 = re.match('\W','ac')
m12 = re.match('\d?','14')
m13 = re.match('\D','_')
print(m10,m11,m12,m13)
m14 = re.match('fuck|duck','duck')
m15 = re.match('(ezgg)+','ezggezgg')
m16 = re.match('(abb)+a','abbabbacabb')
print(m14,m15,m16)
m17 = re.match('\s'," ")
m18 = re.match('[^\S]',' ')
print(m17,m18)
m19 =re.match('\*','*')
m20 = re.match('\a','a')
print(m19,m20)
m21 = re.search('[3-9]{5}','0123456789')
m22 = re.search('^[a-z]{3}','asd123')
m23 = re.search('(123){2}$','123123123')
print(m21,m22,m23)
m24 = re. findall(' [0-9]{4}',"080-0000-9999")
m25 = re. findall('\d{3}', "070-0000-9999")
m26 =re.findall('\d',"算数60点、国語20点")
m27 = re.findall('\d{2,3}',"算数60点、国語20点、英語100点")
m28 = re.findall('[a-zA-Z]',"算数60点、国語20点、英語100点")
print(m24,m25,m26,m27,m28)



print("--------")
#1
text1 = "連絡先は、test@example.com と sales.dept@company.co.jp です。"
result1 = re.findall('([\w.]+\@[\w.]+.[a-z])',text1)
print(result1)


print("--------")
#2
text2 = "問い合わせ先:080-1234-5678、090-8765-4321"
result2 = re.sub('(\d{3}-\d{4}-\d{4})','***-****-****',text2)
print(result2)

print("--------")
#3
text3 = "予定日は2024/01/15で、締切は2024/02/28です。ただし2024/13/32は存在しません。"
result3 = re.findall('[\d]+\/(?:0[1-9]|1[0-2])\/(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])',text3)
print(result3)

print("--------")
#4
text4 = "リンク集:https://example.com, http://test.com, ftp://invalid.com"
result4 = re.findall('https?\://[\w]+\.[\w]+',text4)
print(result4)

print("--------")
#5
text5 = "abc123def456ghi789"
result5 = re.split('\d+',text5)
print(result5)

t_11 =re.search('[\w\D]*','01a-//11_1')
print(t_11)
t_12 =re.findall('[\w]+[^/]+','2024年12月10日,2024/12/20')
print(t_12)
t_13 = re.match('[\d]+年[\d]+月[\d]+日','2024年12月10日')
print(t_13)
t_14 = re.match('\x49',"I")
print(t_14)

print(hex(ord("@")))
#print(hex("0x40"))
