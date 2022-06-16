import json
import requests
import jsonpath
import pymysql
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}

url='https://1680250.com/api/pks/getPksDoubleCount.do?date=&lotCode=10012'

res = requests.get(url,headers=headers)

result = res.content.decode('utf-8')

with open('qishu.json','w',encoding='utf-8')as fp:
    fp.write(result)

obj = json.load(open('qishu.json','r',encoding='utf-8'))

hapma_list = jsonpath.jsonpath(obj,'$..preDrawCode')
yikai= jsonpath.jsonpath(obj,'$..drawCount')
qishu=jsonpath.jsonpath(obj,'$..preDrawIssue')
print(hapma_list)
db = pymysql.connect(host="185.250.221.219", user="root", password="root", database="azxy10ku")
cursor = db.cursor()
cursor.execute("insert into kaijiang(caizhong,qishu,kaihaoma)values(%s,%s,%s)", ('azxy', qishu, hapma_list))
db.commit()