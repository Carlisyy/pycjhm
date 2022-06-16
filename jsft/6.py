import json
import requests
import jsonpath
import pymysql
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}
second=5

while True:
    url = 'https://1680250.com/api/expertsRecommend/list.do?lotCode=10035&groupCode=1&ranking=6&type=0&field=winningProbability&sort=desc'
    res = requests.get(url, headers=headers)
    result = res.content.decode('utf-8')
    with open('ranking6.json', 'w', encoding='utf-8') as fp:
        fp.write(result)
    obj = json.load(open('ranking6.json', 'r', encoding='utf-8'))
    hapma_list = jsonpath.jsonpath(obj, '$..recommendCode')
    qihao = jsonpath.jsonpath(obj, '$..preDrawIssue')
    print(qihao[0])
    print(hapma_list[0])
    db = pymysql.connect(host="185.250.221.219", user="root", password="root", database="azxy10ku")
    cursor = db.cursor()
    cursor.execute("insert into jisujihua(rank,qihao,haoma)values(%s,%s,%s)", (6, qihao[0], hapma_list[0]))
    db.commit()
    time.sleep(second)