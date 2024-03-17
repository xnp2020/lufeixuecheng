#!/usr/bin/env python3
# coding=utf-8


import json


def validate_phone(num):
    if not num.isdigit():
        exit('手机号必须是数字！')
    if len(num) != 11:
        exit('手机号必须是11位！')


courses = ['Python', 'Linux', '网络安全', '前端', '数据分析']
with open('output.json', 'r') as f:
    users = json.load(f)


phones = list(users.keys())

IDs = [value['ID'] for value in users.values()]


name = input('请输入姓名：').strip()
age = int(input('请输入年龄：').strip())

phone = input('请输入手机号，必须唯一：')
validate_phone(phone)
while 1:
    if phone not in phones:
        phones.append(phone)
        break
    else:
        phone = input('手机号已存在，请重新输入：')

ID = input('请输入身份证号，必须唯一：')
while 1:
    if ID not in IDs:
        IDs.append(ID)
        break
    else:
        ID = input('身份证号已存在，请重新输入：')

course = input('请输入课程，只能是(Python/Linux/网络安全/前端/数据分析)之一：')
while 1:
    if course not in courses:
        course = input('课程只能是(Python/Linux/网络安全/前端/数据分析)之一，请重新输入：')
    else:
        break


users[phone] = {'name': name, 'age': age,
                'phone': phone, 'ID': ID, 'course': course}


# 将字典写入文件
with open('output.json', 'w') as f:
    json.dump(users, f, indent=4)
