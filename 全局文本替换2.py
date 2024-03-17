import sys


def replace_in_file(file_path, old_str, new_str):
    # 初始化替换计数器
    replace_count = 0

    # 逐行读取文件内容并替换
    with open(file_path, 'r', encoding='utf-8') as file:
        # 创建一个临时文件保存修改后的内容
        with open(file_path + '.tmp', 'w', encoding='utf-8') as tmp_file:
            for line in file:
                modified_line, count = line.replace(
                    old_str, new_str), line.count(old_str)
                tmp_file.write(modified_line)
                replace_count += count

    # 用修改后的临时文件覆盖原始文件
    import os
    os.replace(file_path + '.tmp', file_path)

    return replace_count


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_path> <old_str> <new_str>")
        sys.exit(1)

    file_path = sys.argv[1]
    old_str = sys.argv[2]
    new_str = sys.argv[3]

    replaced_count = replace_in_file(file_path, old_str, new_str)
    print(f"替换完成。共替换了 {replaced_count} 处地方。")
