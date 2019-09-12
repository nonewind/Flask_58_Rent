# -*- coding: utf-8 -*-
# @ ziheng_wind

import sqlite3
import requests
import re
from bs4 import BeautifulSoup
import time

class Fuck_58():
    def __init__(self,url):
        self.url = url
        self.list_loc = []


    def Sqlite_W(self):
        DBDATA = 'D:\CODE/flask_text/data_loc.db'
        connect = sqlite3.connect(DBDATA)
        sql_cc = connect.cursor()
        for line in self.list_loc:
            try:
                sql = "INSERT INTO Qingdao_0 values('{}')".format(line)
                sql_cc.execute(sql)
            except:
                continue
            print(sql)
            connect.commit()
        sql_cc.close()
    def req_get(self):
        headers = {
            'Host': 'm.58.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'accept-language': 'zh-CN,zh;q=0.9'}
        req = requests.get(self.url,headers=headers).text
        req_bf = BeautifulSoup(req,'html.parser')
        req_data = req_bf.find_all("li",class_="list-item-info-title strongbox")
        re_bat = '[\S]室[\S]厅[\S]卫'
        for line in req_data:
            row = str(line)
            row = row.replace('<li class="list-item-info-title strongbox">',"")
            row = row.replace("</li>",'')
            row = row.replace(" ",'')
            row = row.replace("\n",'')
            row_re = re.sub(re_bat,"",row)
            self.list_loc.append(row_re)
            
def contral():
    DBDATA = 'D:\CODE/flask_text/data_loc.db'
    connect = sqlite3.connect(DBDATA)
    sql_cc = connect.cursor()
    sql = " DELETE FROM Qingdao_0"
    sql_cc.execute(sql)
    connect.commit()
    sql_cc.close()


    page_number = 0
    while page_number<=55:
        if page_number == 0:
            url = 'https://m.58.com/qd/zufang/0/b3/'
        else:
            url = 'https://m.58.com/qd/zufang/0/b3/pn{}'.format(page_number)
        print(page_number)
        Og = Fuck_58(url)
        Og.req_get()
        Og.Sqlite_W()
        page_number+=1
        time.sleep(3)
        
if __name__ == "__main__":
    contral()