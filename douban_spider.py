#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :douban_spider.py
@说明        :
@时间        :2024/03/14 07:12:21
@作者        :xnp2010
@版本        :1.0
'''

import re
import requests
import bs4


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}


def download_page(url):

    page_objs = requests.get(url, headers=headers)
    bs4_obj = bs4.BeautifulSoup(page_objs.text, 'lxml')

    url_set = set()
    paginator_ele = bs4_obj.find('div', attrs={'class': 'paginator'})
    # print(paginator_ele)
    if paginator_ele:
        for a_ele in paginator_ele.find_all('a'):
            url_set.add(a_ele.attrs.get('href'))

        bs4_page_obj_list = [bs4_obj]
        for url in url_set:
            print(f'下载分页{url}')
            page_obj = requests.get(url, headers=headers)
            bs4_page_obj = bs4.BeautifulSoup(page_obj.text, 'lxml')
            bs4_page_obj_list.append(bs4_page_obj)

    return bs4_page_obj_list


def fetch_emails(page_obj_list):
    mail_list = []
    for bs4_obj in page_obj_list:
        comment_eles = bs4_obj.find_all('div', attrs={'class': 'reply-doc'})
        for ele in comment_eles:
            comment_ele = ele.find('p', attrs={'class': 'reply-content'})
            email_addr = re.search(r'\w+@\w+\.\w+', comment_ele, flags=re.A)
            if email_addr:
                pub_time = ele.find('span', attrs={'class': 'pubtime'})
                mail_list.append([pub_time, email_addr.group()])
