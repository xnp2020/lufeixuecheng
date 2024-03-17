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


def download_page(url):  # 获取所有分页并将其解析
    bs4_obj_list = []
    page_objs = requests.get(url, headers=headers)
    bs4_obj = bs4.BeautifulSoup(page_objs.text, 'lxml')
    bs4_obj_list.append(bs4_obj)

    paginator_obj = bs4_obj.find('div', attrs={'class': 'paginator'})
    if paginator_obj:  # 有分页才做
        url_set = set()
        a_eles = paginator_obj.find_all('a')
        for a_ele in a_eles:
            url_set.add(a_ele.attrs.get('href'))

        for url in url_set:
            page_objs = requests.get(url, headers=headers)
            bs4_obj = bs4.BeautifulSoup(page_objs.text, 'lxml')
            bs4_obj_list.append(bs4_obj)

    return bs4_obj_list


def fetch_mail(bs4_obj_list):  # 从解析后的文件中获取发帖时间和email地址
    mail_list = []
    for bs4_obj in bs4_obj_list:
        comment_eles = bs4_obj.find_all('div', attrs={'class': 'reply-doc'})

        for ele in comment_eles:
            comment_ele = ele.find('p', attrs={'class': 'reply-content'})
            email_addr = re.search(
                r'\w+@\w+\.\w+' + '|' + r'[0-9]{6,}', comment_ele.text, flags=re.A)  # 匹配邮箱或数字
            if email_addr:
                if '@' not in email_addr.group():
                    pub_time = ele.find('span', attrs={'class': 'pubtime'})
                    mail_list.append(
                        [pub_time.text, email_addr.group()+'@qq.com'])
                else:
                    pub_time = ele.find('span', attrs={'class': 'pubtime'})
                    mail_list.append([pub_time.text, email_addr.group()])

    return mail_list


if __name__ == '__main__':
    with open('mail.txt', 'w', encoding='utf-8') as f:
        bs4_obj_list = download_page(
            'https://www.douban.com/group/topic/102840294')
        emails = fetch_mail(bs4_obj_list)
        for m in emails:
            line = ' '.join(m)
            f.write(line + "\n")
