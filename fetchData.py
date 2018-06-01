import requests
import json
import datetime
import pymongo
from pymongo import MongoClient
client = MongoClient('192.168.17.52', 27050)
db = client.db_coin


import time
import sched



def main():
    print "start:\n"
    sch()

def sch():
    time.sleep(2)
    ts = time.time()
    sec = int(ts)
    will = (-sec) % 3600
    s = sched.scheduler(time.time, time.sleep)
    print('sched will start after ' + str(will/60) + 'minutes')
    s.enter(will, 0, ru, ())
    s.run()

def ru():
    print("will get coin now!")
    print(datetime.datetime.fromtimestamp(time.time()))
    try:
        httpget()
    except Exception, e:
        print e.message
    sch()



def httpget():

    ld = []
    collection = db.cl_okex_btcusdt_1min
    last = collection.find().sort("_id", pymongo.DESCENDING).limit(1)
    lastObj = last.next()
    lastts = lastObj['_id']
    url = "https://www.okex.com/api/v1/kline.do?symbol=btc_usdt&type=1min&since=" + str(lastts)
    proxies = {"http": "http://192.168.17.62:3128", "https": "https://192.168.17.62:3128", }
    response = requests.get(url, proxies=proxies)
    data = json.loads(response.content)
    print(data)
    for d in data:
        ts = d[0]
        open = float(d[1])
        high = float(d[2])
        low = float(d[3])
        close = float(d[4])
        amount = float(d[5])
        fm = datetime.datetime.fromtimestamp(ts/1000)
        year = fm.year
        month = fm.month
        day = fm.day
        date = fm.weekday()
        hour = fm.hour
        min = fm.minute
        sec = fm.second
        doc = {"_id": ts, 'open': open, 'high': high, 'low': low, 'close': close}
        collection.save(doc)
        if ld.__len__() > 0:
            up = (close - float(ld[4]))/close*100
            print(up)

        ld = d




main()