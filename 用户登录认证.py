#!/usr/bin/env python3
# coding=utf-8

import getpass

# 文件转字典


def read_user_info(filename):
    users = {}
    with open(filename, 'r') as file:
        for line in file:
            username, password, status = line.strip().split(',')
            users[username] = {'password': password, 'status': status}
    return users

# 字典转文件


def write_user_info(filename, users):
    with open(filename, 'w') as file:
        for username, info in users.items():
            file.write(f"{username},{info['password']},{info['status']}\n")


user_pass_dict = read_user_info('userpass.txt')

while 1:
    username = input('请输入用户名：')
    password = getpass.getpass("请输入密码：")
    if username in user_pass_dict:  # 判断用户名是否存在
        if user_pass_dict[username]['status'] == '0':  # 判断用户状态: 1 为锁定，0 为正常
            count = 0
            while count < 2:
                if password == user_pass_dict[username]['password']:
                    print('登录成功！')
                    break
                else:
                    password = getpass.getpass("密码不正确，请重新输入：")
                count += 1

            if count == 2:  # 3次密码错误
                user_pass_dict[username]['status'] = '1'
                write_user_info('userpass.txt', user_pass_dict)

        else:
            print('账号已锁定！')

    else:
        print('不存在的用户名！')
