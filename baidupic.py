import re, time
import requests as rs
from PIL import Image
from io import BytesIO

rs.adapters.DEFAULT_RETRIES = 1
word = raw_input('Please input a word to search: ')
purl = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%s' % (word, )
r = rs.get(purl)


purlli = re.findall('"objURL":"(.*?)"', r.text, re.S)
headers = {'Connection': 'close', }

for i,v in enumerate(purlli):
    cc = ''
    while True:
        try:
            cc = rs.get(v, headers=headers).content
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 10 seconds")
            print("ZZzzzz...")
            time.sleep(10)
            print("Was a nice sleep, now let me continue...")
            continue
    try:
        pic = Image.open(BytesIO(cc))
        nm = word + str(i) + '.' + pic.format
        pic.save(nm)
    except:
        continue