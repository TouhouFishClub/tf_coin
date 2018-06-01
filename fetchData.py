import requests
import json
import datetime

def main():
    print "start:\n"
    httpget()




def httpget():
    url = "https://www.okex.com/api/v1/kline.do?symbol=btc_usdt&type=1min"
    proxies = {"http": "http://192.168.17.62:3128", "https": "https://192.168.17.62:3128", }
    response = requests.get(url, proxies=proxies)
    data = json.loads(response.content)
    print(data[0])
    ld = []
    for d in data:
        ts = d[0]
        open = float(d[1])
        high = float(d[2])
        low = float(d[3])
        close = float(d[4])
        amount = float(d[5])
        fm = datetime.datetime.fromtimestamp(ts/1000)
        print(ts, open, high, low, close, amount, fm)
        year = fm.year
        month = fm.month
        day = fm.day
        date = fm.weekday()
        hour = fm.hour
        min = fm.minute
        sec = fm.second
        print(year, month, date, hour, min, sec, day)
        if ld.__len__() > 0:
            up = (close - float(ld[4]))/close*100
            print(up)

        ld = d




main()