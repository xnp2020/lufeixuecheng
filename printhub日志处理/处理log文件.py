import zipfile
import os


def myzipfile(zip_file, extract_to):
    # 打开 ZIP 文件
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # 解压所有文件到目标目录
        zip_ref.extractall(extract_to)
    print(f"{zip_file} 解压完成")


root_dir = r'C:\Users\xnp2010\Documents\WeChat Files\wxid_7zt3seoqst7522\FileStorage\File\2024-03\printhub\printhub\10.20.33.10\printhub'

# 用于存储所有文件名的列表
file_names = []

# 使用 os.walk() 遍历目录树
for root, dirs, files in os.walk(root_dir):
    # 将当前目录下的文件名添加到列表中
    for file in files:
        file_names.append(os.path.join(root, file))

# 打印所有文件名
for file_name in file_names:
    if 'zip' in file_name:
        myzipfile(file_name, root_dir)

# 要处理的日志文件
need_log_files = []
for file in os.listdir(root_dir):
    file_path = os.path.join(root_dir, file)
    if os.path.isfile(file_path):
        need_log_files.append(file_path)
