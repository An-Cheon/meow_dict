# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 16:11
# @Author  : An Cheon
# @File    : main.py
import pickle
import os
import sys
import cursor

cursor.hide() # 让光标不闪烁
path = sys.path[0] + "/"
with open(path + 'data/words.data','rb') as f:
    words = pickle.load(f)

with open(path + 'data/meanings.data','rb') as f:
    meanings = pickle.load(f)

def clear():#清空cmd
    os.system('cls')

while True:
    given_words = input("")
    if words.__contains__(given_words):
        clear()
        print(meanings[words.index(given_words)])
    else:#可以增添错词近似处理
        clear()
        print("meow~")