#!/usr/bin/env python3
# coding=utf-8


import random

# 中文姓氏列表
surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯',
            '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许']

# 中文名字列表
names = ['晨', '蕾', '帆', '峰', '梅', '雪', '军', '芳', '波',
         '燕', '涛', '琴', '飞', '华', '明', '丽', '刚', '洁', '浩', '萍']

# 生成300个中文名字
all_stuff = set()  # 使用集合来确保生成的名字不重复

while len(all_stuff) < 300:
    surname = random.choice(surnames)
    name = random.choice(names)
    full_name = surname + name
    all_stuff.add(full_name)

all_stuff = sorted(all_stuff)
print(all_stuff)
print()

input('按下回车键抽取三等奖...')
third_pride = random.sample(all_stuff, 30)
print(f'三等奖：{third_pride}\r\n')
for stuff in third_pride:
    all_stuff.remove(stuff)


input('按下回车键抽取二等奖...')
second_pride = random.sample(all_stuff, 6)
print(f'二等奖：{second_pride}\r\n')
for stuff in second_pride:
    all_stuff.remove(stuff)

input('按下回车键抽取一等奖...')
first_pride = random.sample(all_stuff, 3)
print(f'一等奖：{first_pride}\r\n')
for stuff in first_pride:
    all_stuff.remove(stuff)
