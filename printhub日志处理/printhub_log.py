#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :printhub_log.py
@说明        :
@时间        :2024/03/15 15:53:00
@作者        :xnp2010
@版本        :1.0
'''


import sys
import signal
import multiprocessing
from datetime import datetime
import re
import time
import zipfile
import os

'''
先获取要处理的日志文件
'''


def unzipfile(zip_file, extract_to):  # 解压 ZIP 文件到指定目录
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # 解压所有文件到目标目录
        zip_ref.extractall(extract_to)


def all_files(root_dir):  # 获取目录下所有的日志文件
    # 用于存储所有文件名的列表
    file_names = []

    # 使用 os.walk() 遍历目录树
    for root, dirs, files in os.walk(root_dir):
        # 将当前目录下的文件名添加到列表中
        for file in files:
            file_names.append(os.path.join(root, file))

    # 打印所有文件名
    for file_name in file_names:
        if 'zip' in file_name:  # 解压zip文件到root_dir
            unzipfile(file_name, root_dir)

    # 要处理的日志文件
    need_log_files = []
    for file in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file)
        if os.path.isfile(file_path):
            need_log_files.append(file_path)

    return need_log_files


def delay_job_stat(need_log_file, lock, dest_file):  # 处理文件，并将结果写入文件
    func_begin_time = time.time()
    # 找到文件中所有的job_id
    pattern = re.compile(r'(?<=jobid\s)[a-fA-F0-9]{32}(?=\s未在分布式队列中)')

    with open(need_log_file, 'r', encoding='utf-8') as f:
        job_id_list = pattern.findall(f.read())

    # 找出处理时长超过2秒的job_id
    pattern_1 = re.compile(r'打印作业 @.*false')
    pattern_2 = re.compile(r'未在分布式队列中')

    job_id_dict = {}
    for job_id in job_id_list:
        with open(need_log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                match_1 = pattern_1.search(line)
                if match_1 and job_id in line:
                    job_id_dict[job_id] = [line[:23]]

                match_2 = pattern_2.search(line)
                if match_2 and job_id in line:
                    job_id_dict[job_id].append(line[:23])

    have_2_time_job_cnt = 0  # 统计job_id有2个时间的数量
    delay_job_cnt = 0  # 统计延迟打印的job_id数量

    file_stat_result = f'当前处理的日志：{need_log_file}\n'
    for key, value in job_id_dict.items():
        if len(value) == 2:
            have_2_time_job_cnt += 1
            start_time = datetime.strptime(
                value[0], '%Y-%m-%d %H:%M:%S.%f')
            end_time = datetime.strptime(value[1], '%Y-%m-%d %H:%M:%S.%f')
            delay_time = (end_time - start_time).total_seconds()
            if delay_time > 2:
                delay_job_cnt += 1
                file_stat_result += f'{key} {value} {delay_time} 秒\n'

    file_stat_result += f'延迟打印超过2秒的作业数: {delay_job_cnt}\n'
    file_stat_result += f'job_id有2个时间的数量: {have_2_time_job_cnt}\n'
    file_stat_result += f'作业总数：{len(job_id_list)}\n\n'

    with open(dest_file, 'a', encoding='utf-8') as f:
        lock.acquire()  # 获取文件锁
        try:
            f.write(file_stat_result)
        finally:
            lock.release()  # 释放文件锁
    func_end_time = time.time()
    print(f'处理文件{need_log_file}消耗时长{round(func_end_time-func_begin_time,2)}秒')


def signal_handler(signum, frame):  # 处理Ctrl+c信号
    print(f"Received signal {signum}, stopping all processes")
    for process in multiprocessing.active_children():
        process.terminate()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    lock = multiprocessing.Lock()

    # 指定要处理的目录
    root_dir = r'C:\Users\xnp2010\Documents\WeChat Files\wxid_7zt3seoqst7522\FileStorage\File\2024-03\printhub\printhub\10.20.33.10\printhub'
    dest_file = '10.20.33.10.txt'
    # 从目录中提取要处理的日志文件
    need_log_files = all_files(root_dir)

    processes = []

    for need_log_file in need_log_files:
        p = multiprocessing.Process(
            target=delay_job_stat, args=(need_log_file, lock, dest_file))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print("All processes finished")
