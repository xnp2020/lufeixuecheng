#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :printer_spider.py
@说明        :
@时间        :2024/03/14 10:00:01
@作者        :xnp2010
@版本        :1.0
'''

import requests
import bs4


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'vm=Html; bm=Low; selno=Zh-CN; wd=n; help=off,off,off; bv=Chrome/122.0.0.0; uatype=NN; lang=Zh-CN; favmode=false; param=; access=; ver_expires=Fri, 14 Mar 2025 19:09:28 GMT; ID=sSuXZzghLBsjl1AepINgjlRAZBv9Oedz; usr=S_COU',
    'Host': '192.168.72.65',
    'Referer': 'http://192.168.72.65/wcd/system_device.xml',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}


page_objs = requests.get(
    'http://192.168.72.65/wcd/system_counter.xml', allow_redirects=True)
print(page_objs.status_code)
print(page_objs.history)
bs4_obj = bs4.BeautifulSoup(page_objs.text, 'lxml')
print(bs4_obj.find('table', attrs={'class': 'data-table'}))
