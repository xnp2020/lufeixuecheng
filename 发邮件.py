'''
Author: xnp\xnp2010 xnp2010@qq.com
Date: 2024-03-08 14:44:40
LastEditors: xnp\xnp2010 xnp2010@qq.com
LastEditTime: 2024-03-08 17:20:40
FilePath: \lufeixuecheng\发邮件.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 设置发件人、收件人和邮件内容
sender_email = "nianping.xia@insolu.cn"
receiver_emails = ['nianping.xia@insolu.cn', 'xnp2010@qq.com']
password = "PCgRaG3HteehUJLN"

subject = "Test Email from Python"
body = "Hello, this is a test email sent from Python!"

# 创建邮件对象
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)
message["Subject"] = subject

# 添加邮件正文
message.attach(MIMEText(body, "plain"))

# 连接到SMTP服务器并发送邮件
try:
    server = smtplib.SMTP("smtp.exmail.qq.com", 587)  # 设置SMTP服务器地址和端口号
    server.starttls()  # 开启TLS加密
    server.login(sender_email, password)  # 登录邮箱
    server.sendmail(sender_email, receiver_emails, message.as_string())  # 发送邮件
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
finally:
    server.quit()  # 关闭连接
