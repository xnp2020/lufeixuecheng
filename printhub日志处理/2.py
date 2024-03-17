import re


def delay_job_ids(need_log_file):  # 找到文件中所有的job_id
    pattern = re.compile(r'(?<=jobid\s)[a-fA-F0-9]{32}(?=\s未在分布式队列中)')

    with open(need_log_file, 'r', encoding='utf-8') as f:
        job_id_list = pattern.findall(f.read())

    return job_id_list


need_log_file = 'C:\\Users\\xnp2010\\Documents\\WeChat Files\\wxid_7zt3seoqst7522\\FileStorage\\File\\2024-03\\printhub\\printhub\\10.20.33.10\\printhub\\printhub.log'
print(len(delay_jobs(need_log_file)))
