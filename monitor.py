#coding:utf-8
'''
Created on 2017年4月11日
@author: superxiaoxiong
'''

import time
import MySQLdb

#--------数据库添加-------
'''
使用python原生语句操作mysql数据库
'''
python_conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd = 'root',db='webuser')
python_cur = python_conn.cursor()
python_conn.autocommit(True)


def getMem():
    with open('/proc/meminfo') as f:
        
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = total - free - buffers - cache
    t = int(time.time())
    sql = 'insert into monitor (memory,time) value (%s,%s)' % (mem_use/1024,str(t))
    python_cur.execute(sql)
    print mem_use/1024
    
   
while True:
    time.sleep(1)
    getMem()
    
