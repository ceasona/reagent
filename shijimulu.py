import re
from bs4 import BeautifulSoup
import requests
import os
import time
# currentPath = "E:/regent/shijimulu.py"
# # 分离文件路径与文件名的方法
# wewe = re.findall(r'.+\/',currentPath)[0]
# # print(wewe)
reagent="22374-89-6"

session = requests.session()
def spiderData(reagent):
    url = 'https://www.energy-chemical.com/search.html?key=' + reagent
    headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
     "Accept": "*/*",
     "Accept-Encoding": "gzip, deflate",
     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
     "Cache-Control": "no-cache",
     "Connection": "akeep-alive"
    }

    data = session.get(url=url,headers=headers)
    a = data.text
    soup = BeautifulSoup(a, 'lxml')
    allContent = soup.select('tbody > tr >td')
    name_Chinese = re.findall("(.+)\(订货以英文名称为准\)",allContent[2].get_text())[0]
    name_English = re.findall("(.+)\(订货以英文名称为准\)", allContent[4].get_text())[0]
    arry = [name_Chinese, name_English,allContent[6].get_text(), allContent[10].get_text(), allContent[12].get_text()]
    print(arry)

# spiderData(reagent)
# if os.path.exists("D:/user/Desktop/readContent.xls"):
#     print("cunzai")

# ti = time.time()
# print(round(ti))

spiderData(reagent)