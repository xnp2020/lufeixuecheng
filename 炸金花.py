#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :炸金花.py
@说明        :
@时间        :2024/03/07 14:06:10
@作者        :xnp2010
@版本        :1.0
'''
import random


cards = ['小王', '大王']
card_colors = ['♠', '♥', '♣', '♦']
card_nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for m in card_colors:
    for n in card_nums:
        cards.append(m+n)

players = int(input('请输入玩家数量：').strip())
for i in range(players):
    selected_cards = random.sample(cards, 3)
    print(f'{i+1}号玩家：', selected_cards)
    for card in selected_cards:
        cards.remove(card)
