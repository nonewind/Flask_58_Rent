# -*- coding: utf-8 -*-
# 张子恒

import datetime
import json
import random
import re
import time

import requests
from pymongo import MongoClient

client = MongoClient('mongodb://149.129.121.154')
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
            # 爬虫抓取日期 为了以后的解决数据冗余问题而设置的字段
            # 解决数据冗余 筛选出日期在30天以上的数据 直接删除掉
            update = datetime.datetime.today().date()
            # 价格等级
            for row in range(1, 21, 1):
                # 页面深度
                print(line['city_zh']+"价格等级"+str(item)+"的第"+str(row)+"个页面")
                url = "https://m.58.com/{}/chuzu/b{}/pn{}/".format(
                    line['city_58'], str(item), str(row))
                req = requests.get(url, headers=headers)
                if "404" not in req.url and "callback" not in req.url:
                    print("成功抓取")
                    # 格式化返回的string
                    req_replace = req.text.replace(
                        "\n", "").replace("\t", "").replace(" ", "")
                    # 飞两个正则 飞出title和url
                    bat_title = r'<spanclass=\"list-item-info-addr-textstrongbox\">[\s\S]{1,50}</span>'
                    bat_url = r'<aclass=\"list-item\"href=\"[\s\S]{1,1000}\"tongji_tag='
                    title_all = re.compile(bat_title).findall(req_replace)
                    url_all = re.compile(bat_url).findall(req_replace)
                    # 生成器+repalce 输出想要的字符 -> list()
                    title_all_return = [x.replace(
                        '<spanclass="list-item-info-addr-textstrongbox">', '').replace('</span>', '') for x in title_all]
                    url_all_return = [y.replace(
                        '<aclass="list-item"href="', '').replace('"tongji_tag=', '') for y in url_all]
                    # 去掉title中的 x室
                    bat_title_x = r'[\d]室'
                    title_all_new = [re.sub(bat_title_x, '', xxxx)
                                     for xxxx in title_all_return]
                    print("开始尝试插入数据库")
                    for nn in range(100):
                        try:
                            data = {
                                "title": title_all_new[nn],
                                "url": url_all_return[nn],
                                "priceLevel": row,
                                "cityname": line['city_zh'],
                                "update": str(update)
                            }
                            mongoDB_insert(data)
                        except:
                            break
                else:
                    print("抓取失败")
                    pass
                print("休眠一下")
                time.sleep(random.uniform(10, 20))  # 随机休眠20~60s


def mongoDB_insert(data):
    coll.insert_one(data)


def city_get():
    coll = db['spider_task']
    data = coll.find()[0]["city_task"]
    return data  # data ->list


if __name__ == "__main__":
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'f=n; f=n; f=n; listCalledApp=true; f=n; 58home=qd; id58=c5/nfF/1CCNv0++LCce7Ag==; 58tj_uuid=25f9770b-45a0-4257-8f4b-29e75f26faad; als=0; wmda_new_uuid=1; wmda_uuid=ff169493500dcfd5c7988bce040890b1; wmda_visited_projects=%3B11187958619315; xxzl_deviceid=TxQ0vmXmtYX6HHI2Hf0C1Zvn%2BRG9IHZBQ1DhdyHQ%2Flfxaz6zroyvR7lHBvzthpql; myfeet_tooltip=end; Hm_lpvt_3f405f7f26b8855bc0fd96b1ae92db7e=1610011309; Hm_lvt_3f405f7f26b8855bc0fd96b1ae92db7e=1610003453,1610010657,1610010678,1610011309; ppStore_fingerprint=5EDD06E1E476BDCF36EC6E5916965D4B76A00CAB97AFBCC5%EF%BC%BF1610011310893; f=n; mcityName=%u9752%u5C9B; mcity=qd; selectcity=yes; city=qd; new_uv=6; utm_source=; spm=; init_refer=; wmda_session_id_11187958619315=1610073118222-ccbc6cb1-27a3-f7b0; xxzl_cid=c30d20d44aa54551bbb220b2ba33aae9; xzuid=c4cc2124-c249-49e9-8380-1d52375492a1; new_session=0; qz_gdt=; _house_detail_show_time_=3',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    spider_main()
