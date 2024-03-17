#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :word操作.py
@说明        :
@时间        :2024/03/11 16:55:26
@作者        :xnp2010
@版本        :1.0
'''

from docx import Document  # pip install docx


def find_text_in_docx(docx_file, text_to_find):
    doc = Document(docx_file)
    found = False

    for paragraph in doc.paragraphs:
        if text_to_find in paragraph.text:
            found = True
            print(f"Found '{text_to_find}' in paragraph: '{paragraph.text}'")
            # 如果您只想找到第一个匹配项，可以取消注释下面的return语句
            # return

    if not found:
        print(f"'{text_to_find}' not found in the document.")


# 调用函数来查找特定文本
find_text_in_docx("example.docx", "Hello, World!")
