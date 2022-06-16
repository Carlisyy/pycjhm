import json
import requests
from bs4 import BeautifulSoup
import lxml
import os
import jsonpath
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
}

url='https://1680250.com/api/pks/queryToDayNumberLawOfStatistics.do?date=&lotCode=10012'

res = requests.get(url,headers=headers)

result = res.content.decode('utf-8')

with open('rank.json','w',encoding='utf-8')as fp:
    fp.write(result)

obj = json.load(open('rank.json','r',encoding='utf-8'))

hapma_list = jsonpath.jsonpath(obj,'$...accumulate')

print(hapma_list)
guanjun=[]

for i in range(0,len(hapma_list),10):
    print(hapma_list[i])
    guanjun.append(hapma_list[i])


print(guanjun)
zongshu=sum(guanjun)
print(zongshu)
haoma1=guanjun[0]/zongshu
haoma2=guanjun[1]/zongshu
haoma3=guanjun[2]/zongshu
haoma4=guanjun[3]/zongshu
haoma5=guanjun[4]/zongshu
haoma6=guanjun[5]/zongshu
haoma7=guanjun[6]/zongshu
haoma8=guanjun[7]/zongshu
haoma9=guanjun[8]/zongshu
haoma10=guanjun[9]/zongshu
print(haoma1,haoma2,haoma3,haoma4,haoma5,haoma6,haoma7,haoma8,haoma9,haoma10)
