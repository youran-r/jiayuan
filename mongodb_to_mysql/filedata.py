# -*- coding:utf-8 -*- 
import MySQLdb
import json
file = open("/tmp/file.bak")
 
cxn = MySQLdb.Connect(host = '127.0.0.1', user = 'root', passwd = 'youran2018', db='jiayuan',charset='utf8')
cur = cxn.cursor()

# 判断是否为数字
def isNum(value):
    try:
        value+1
    except TypeError:
        return False
    else:
        return True

while 1:
    line = file.readline()
    if not line:
        break
    arr = json.loads(line)
 
    insert_sql = 'insert into user set '
    for k in arr:
        if k == '_id':
            arr[k] = arr[k]['$oid']
        if arr[k] and not isNum(arr[k]):
            arr[k] = arr[k].replace("'", '')
            arr[k] = arr[k].replace("'", '')
            arr[k] = arr[k].replace("\\", '')
        insert_sql = insert_sql +"%s='%s'," %(k,arr[k])
    insert_sql = insert_sql[:-1]
    try:
        cur.execute(insert_sql)
    except TypeError:
        print insert_sql

print 'done'
cur.close()
cxn.commit()
cxn.close()
exit()

