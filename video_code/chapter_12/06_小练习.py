# 练习一：将一个二进制文件复制到指定位置
# 源文件
# region
# import os
#
# source = 'AI大模型工程师体系课程目录.png'
# # 目标目录
# target = 'D:\\Workspace\\code-python\\python\\video_code\\chapter_12\\demo'
#
# if not os.path.exists(target):
#     os.mkdir(target)
#
# with open(source, 'rb') as f1, open(target + '/' + '1.png', 'wb') as f2:
#     while True:
#     # 二进制文件读完返回的是一个空字节：b'',文本文件返回空字符串
#         data = f1.read(1024)
#         if not data:
#             break
#         # 向目标文件中写入数据
#         f2.write(data)
#     print('复制完毕')
# endregion
import time

# 联系二：日志记录

users = {
    '张三': '123456',
    '李四': '000000',
    '王五': '123456'
}

# 提示输入信息
username = input('请输入用户名：')
password = input('请输入密码：')

now = time.strftime('%Y-%m-%d %H:%M:%S')

if username  not in users:
    print('用户未注册')
    with open('log.txt', 'a+',encoding='utf=8') as file:
        file.write(f'{now}  {username} 登录失败（用户未注册） \n')

elif users[username] != password:
    with open('log.txt', 'a+',encoding='utf=8') as file:
        file.write(f'{now}  {password} 登录失败（密码错误）')
elif users[username] == password:
    with open('log.txt', 'a+',encoding='utf=8') as file:
        file.write(f'{now} {username} 登录成功')