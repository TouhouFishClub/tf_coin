import datetime

import pymongo
from pymongo import MongoClient
client = MongoClient('192.168.17.52', 27050)
db = client.db_coin

def run():
    collection = db.cl_okex_btcusdt_1min
    cursor = collection.find().limit(100).skip(0)
    strx = ""
    while(cursor.alive):
        data = cursor.next()
        ts = data['_id']
        high = data['high']
        low = data['low']
        openx = data['open']
        close = data['close']
        fm = datetime.datetime.fromtimestamp(ts/1000)
        year = fm.year
        month = fm.month
        day = fm.day
        date = fm.weekday()
        hour = fm.hour
        min = fm.minute
        sec = fm.second
        up = (close - openx) / openx * 100 * 100
        d = str(year)+","+str(month)+","+str(day)+","+str(hour)+","+str(min)+","+str(sec)+","+str(date)+","
        d = d+str(openx)+","+str(close)+","+str(high)+","+str(low)+","+str(int(up))
        strx = strx + d + "\n"
    f = open('train1.csv', 'w')
    f.write(strx)
    f.close()


run()