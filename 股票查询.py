#!/usr/bin/env python3
# coding=utf-8


import csv
import re


while 1:
    user_input = input('股票查询接口>>: ')
    with open('stock.txt', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # pattern = r'[><=]'
            # if re.search(pattern, user_input):
            #     compare = re.search(pattern, user_input)[0]
            #     query_string = re.split(rf'{compare}', user_input)[0]
            #     query_num = re.split(rf'{compare}', user_input)[1]
            #     if row[query_string] > query_string and row[]
            if '>' in user_input:
                query_string = user_input.split('>')[0]
                query_num = user_input.split('>')[1]
                if float(row[query_string]) > float(query_num):
                    print(row)
            elif '<' in user_input:
                query_string = user_input.split('<')[0]
                query_num = user_input.split('<')[1]
                if float(row[query_string]) < float(query_num):
                    print(row)
            else:
                pattern = rf'{user_input}'
                if re.search(pattern, row['股票名称']):
                    print(row)
