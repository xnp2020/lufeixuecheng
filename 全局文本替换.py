#!/usr/bin/env python3
# coding=utf-8


import sys
import os


def replace_in_file(old_str, new_str, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        with open(filename+'.tmp', 'w', encoding='utf-8') as tmp_f:
            for line in f:
                tmp_f.write(line.replace(old_str, new_str))
    os.replace(filename+'.tmp', filename)


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) != 4:
        print('脚本使用方法：python 全局文本替换.py old_str new_str filename')
        sys.exit(1)
    old_str = sys.argv[1]
    new_str = sys.argv[2]
    filename = sys.argv[3]
    replace_in_file(old_str, new_str, filename)
