import sqlite3
DBDATA = 'D:\CODE/flask_text/data_loc.db'
table_name = 'Location'

connect = sqlite3.connect(DBDATA)
sql_cc = connect.cursor()

sql = "INSERT INTO Qingdao_0 values('海洋世界')"
sql_cc.execute(sql)
connect.commit()
sql_cc.close()

print("11")