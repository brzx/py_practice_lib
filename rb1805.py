import requests, time

def printRB():
    r = requests.get("http://hq.sinajs.cn/list=RB1805", proxies={"http":"http://proxy-url.com:8080"})
    li = r.text.split("=")[1].split('"')[1].split(',')
    nameli = ['name', 'unKnowNum','startPrice','highPrice','lowPrice','yesterdayPrice','buyOnePrice','sellOnePrice','latestPrice','lastPrice','yesLastPrice','buyQu','sellQu','haveQu','lastQu','state','class','date']
    #for index,l in enumerate(nameli):
    #    print "%-15s is %-20s" % (l, li[index])
    print "=====================The import buy one price is %s=====================" % (li[6],)

if __name__ == '__main__':
    for i in range(10):
        printRB()
        time.sleep(10)
