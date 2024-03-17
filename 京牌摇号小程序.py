#!/usr/bin/env python3
# coding=utf-8

import string
from random import choice, choices

count = 0
while count < 3:
    car_nums = {}

    for i in range(20):
        num1 = choice(string.ascii_uppercase)
        num2 = ''.join(choices(string.ascii_uppercase+string.digits, k=6))
        car_num = f'京{num1}-{num2}'
        car_nums[i+1] = car_num

        print(i+1, car_num)
    print(car_nums)

    your_choice = int(input('请选择您要的车牌：').strip())

    if your_choice in car_nums:
        print(f'恭喜！您选择的车牌号是{car_nums[your_choice]}!')
    else:
        print(f'车牌号不合法，请重新选择！')

    count += 1
