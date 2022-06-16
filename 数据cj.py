import json
import requests
from bs4 import BeautifulSoup
import lxml
import os
import jsonpath

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}

url='https://1680250.com/api/pks/getPksHistoryList.do?date=2022-06-10&lotCode=10012'

res = requests.get(url,headers=headers)

result = res.content.decode('utf-8')

with open('tpp.json','w',encoding='utf-8')as fp:
    fp.write(result)

obj = json.load(open('tpp.json','r',encoding='utf-8')) # 注意，这里是文件的形式，不能直接放一个文件名的字符串

hapma_list = jsonpath.jsonpath(obj,'$..preDrawCode') # 文件对象   jsonpath语法

print(len(hapma_list))