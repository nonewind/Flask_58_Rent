# -*- coding: utf-8 -*-
# @ ziheng_wind

import re
import sqlite3
import time

import requests
from bs4 import BeautifulSoup


def sql_w():
    DBDATA = '/www/wwwroot/map.ziheng.xyz/db_loc.db'
    bx = 2
    while bx <= 4:
        connect = sqlite3.connect(DBDATA)
        sql_cc = connect.cursor()
        sql = " DELETE FROM qingdao_{}".format(bx-2)
        sql_cc.execute(sql)
        connect.commit()
        sql_cc.close()
        page_number = 0

        bool_url = True

        while bool_url:
            print(bx, page_number)
            if page_number == 0:
                url = 'https://m.58.com/qd/zufang/0/b{}/'.format(bx)
            else:
                url = 'https://m.58.com/qd/zufang/0/b{}/pn{}'.format(
                    bx, page_number)

            list_loc = []
            headers = {
                'Host': 'm.58.com',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
                'accept-language': 'zh-CN,zh;q=0.9'}
            req = requests.get(url, headers=headers).text
            req_bf = BeautifulSoup(req, 'html.parser')
            req_data = req_bf.find_all(
                "li", class_="list-item-info-title strongbox")
            re_bat = '[\S]室[\S]厅[\S]卫'
            for line in req_data:
                row = str(line)
                row = row.replace(
                    '<li class="list-item-info-title strongbox">', "")
                row = row.replace("</li>", '')
                row = row.replace(" ", '')
                row = row.replace("\n", '')
                row_re = re.sub(re_bat, "", row)
                list_loc.append(row_re)
            if list_loc:
                
                connect = sqlite3.connect(DBDATA)
                sql_cc = connect.cursor()
                if bx == 2:
                    for line in list_loc:
                        try:
                            sql = "INSERT INTO qingdao_0 values('{}')".format(line)
                            sql_cc.execute(sql)
                        except:
                                continue
                        connect.commit()
                elif bx == 3:
                    for line in list_loc:
                        try:
                            sql = "INSERT INTO qingdao_1 values('{}')".format(line)
                            sql_cc.execute(sql)
                        except:
                                continue
                        connect.commit()
                elif bx == 4:
                    for line in list_loc:
                        try:
                            sql = "INSERT INTO qingdao_2 values('{}')".format(line)
                            sql_cc.execute(sql)
                        except:
                            continue
                        connect.commit()
                sql_cc.close()
                bool_url = True
            else:
                bool_url = False
            page_number += 1
            time.sleep(1)
        bx += 1

if __name__ == "__main__":
    sql_w()