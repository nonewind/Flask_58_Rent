# -*- coding: utf-8 -*-
# 张子恒

import datetime
import random
import re
from threading import excepthook
import time

import requests
from pymongo import MongoClient
from config import MONGO
from bs4 import BeautifulSoup

client = MongoClient(MONGO, connect=False)
db = client["Fuck_58"]
coll = db['spider_result']
"""
还需要解决反爬虫的问题
- 具体表现在需要登录拿cookie
- 需要摸出反爬虫的时间长度
"""


def spider_main():
    listOfCity = city_get()
    # 请求总数 = 20*城市总数*价格等级数
    for line in listOfCity:
        # 城市名
        for item in range(1, 7, 1):  # 12|34|56 - 0|1|2
            # 价格等级
            update = datetime.datetime.today()
            # 价格等级
            for row in range(1, 5, 1):
                # 数据库内无需存放太多数据
                print(line['city_zh'] + "价格等级" + str(item) + "的第" + str(row) + "个页面")
                url = "https://m.58.com/{}/chuzu/b{}/pn{}/".format(line['city_58'], str(item),
                                                                   str(row))
                req = requests.get(url, headers=headers)
                if "404" not in req.url and "callback" not in req.url:
                    print("成功抓取")
                    # 格式化返回的string
                    #req_replace = req.text.replace("\n", "").replace("\t", "").replace(" ", "")
                    # 飞两个正则 飞出title和url
                    bsobj = BeautifulSoup(req.text, 'html.parser')
                    all_tag = bsobj.find_all("li")
                    for row in all_tag:
                        row = str(row).replace("\n", "").replace("\t", "").replace(" ", "")
                        if "strongbox" not in row:continue
                        #line = line.replace("\n", "").replace("\t", "").replace(" ", "")
                        bat_title = r'<spanclass=\"list-item-info-addr-textstrongbox\">[\d]{1,10}室([\s\S]{1,30})</span>'
                        bat_url = r'class=\"list-item\"href=\"([\s\S]{1,300})shangquan='
                        bat_img = r'bg-src=\"([\s\S]{1,200})\"class=\"list-item-img'
                        bat_homeType = r'<liclass=\"list-item-info-titlestrongbox\">([\s\S]{1,2})\|'
                        bat_price = r'<iclass=\"strongbox\">([\d\D]{1,6})</i>'
                        try:
                            price = re.search(bat_price,row).group(1)
                            titel = re.search(bat_title,row).group(1)
                            homeType = re.search(bat_homeType,row).group(1)
                            img = re.search(bat_img,row).group(1)
                            url_goto = re.search(bat_url,row).group(1)
                        except:
                            continue
                        print("开始尝试插入数据库")
                        data = {
                            "title": titel,
                            "url": url_goto,
                            "priceLevel": item,
                            "cityname": line['city_zh'],
                            "price": price,
                            "class":homeType,
                            "img":img,
                            "from":"58",
                            "update": update
                        }
                        print(data)
                        coll.insert_one(data)
                else:
                    print("抓取失败")
                    pass
                print("休眠一下")
                time.sleep(random.uniform(5, 10))  # 随机休眠40~80s

def city_get():
    coll = db['spider_task']
    data = coll.find()[0]["city_task"]
    return data  # data ->list


if __name__ == "__main__":
    headers = {
        'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':
        'gzip, deflate, br',
        'accept-language':
        'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie':
        '58home=bj; id58=c5/nfGC5ws+9P+/XDGI6Ag==; city=bj; 58tj_uuid=d92398d9-3122-4459-9004-71649705467e; als=0; wmda_uuid=b90c68f45eba52ada283c0dbf894d575; wmda_new_uuid=1; wmda_visited_projects=%3B11187958619315; xxzl_deviceid=qtn46pP3OgRANm9sV9iM8fHapK83dF4GY%2BBfQz5nYdzA3UH5JX8Rj%2BUibMgsDJn0; new_uv=2; utm_source=; spm=; init_refer=; wmda_session_id_11187958619315=1622963811553-18571b20-a033-6973; xxzl_cid=efe677af9e7f4aff86c399a043b2937d; xzuid=5b9590a0-5244-4389-bd2f-2907f52655d0; new_session=0; qz_gdt=; f=n; selectcity=yes; mcity=qd; mcityName=%u9752%u5C9B',
        'user-agent':
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    date_clean = (datetime.datetime.today() - datetime.timedelta(hours=12))
    que = {"update": {"$lt":date_clean}}
    for line in coll.find(que):
        print(line)
    coll.delete_many(que)
    spider_main()
