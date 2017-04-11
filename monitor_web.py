#coding:utf-8
'''
Created on 2017年4月11日
@author: superxiaoxiong
'''

import web
import json


urls = (
    '/(.*)/','redirect',
    '/data', 'data',
    '/','index',
    )

def notfound():
    return web.seeother('./index')

app = web.application(urls, globals())
app.notfound = notfound

db1 = web.database(dbn = 'mysql', db='webuser', user='root',pw='root')  

class redirect:
    def GET(self, path):
        web.seeother('/'+ path)


class index:
    def GET(self):
        render = web.template.render('templates')
        return "%s" % (render.index())

class data:
    def GET(self):
        sql = 'select memory,time from monitor '
        results = db1.query(sql )
        arr = []
        for item in results:
            arr.append([item[1]*1000,item[0]])
        return json.dumps(arr)


if __name__ == "__main__":
    app.run()
