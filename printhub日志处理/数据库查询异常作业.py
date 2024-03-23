import mysql.connector
import time

"""
找出处于“处理中”状态过长的作业
"""

# 定义数据库连接参数
db_config = {
    "host": "localhost",
    "port": '3307',
    "user": "root",
    "password": "123456",
    "database": "printhub"

}

fids = []
# 使用with语句管理连接
with mysql.connector.connect(**db_config) as conn:
    # 创建游标对象
    with conn.cursor() as cursor:
        # # 创建一个示例表格
        # cursor.execute('''CREATE TABLE IF NOT EXISTS users
        #                   (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)''')

        # # 插入一些示例数据
        # cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 30))
        # cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Bob', 25))

        # # 提交更改
        # conn.commit()

        # 查询数据
        cursor.execute("SELECT fid FROM t_job where fstatus = 'processing'")
        rows = cursor.fetchall()
        for row in rows:
            fids.append(row[0])

waiting_time = 30
time.sleep(waiting_time)



with mysql.connector.connect(**db_config) as conn:
    with conn.cursor() as cursor:
        for fid in fids:
            cursor.execute("SELECT fid,fname,fsubmittime,flastupdatetime,fstatus FROM t_job where fid = %s",(fid,))
            job = cursor.fetchall()
            if job[0][4] == 'processing':
                print(f'作业{job[0]}在"处理中"状态超过{waiting_time}秒')
           
            