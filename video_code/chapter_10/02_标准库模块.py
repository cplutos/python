# 随着Python一起安装在我们电脑上的那些模块
import copy         #   拷贝对象
import os           #   操作系统相关操作（文件。文件夹等系统层面操作）
import random       #   随机数相关
import time         #   时间相关
import math         #   数学相关
import sys          #   Python解释器相关操作

# os.mkdir('demo')

# 随机选人
names = ['a','b','c','d','e']
print(random.choice(names))

# 洗牌
names = ['a','b','c','d','e']
random.shuffle(names)
print(names)

# 休眠
time.sleep(2)
print('ok')

# 获取当前时间
print(time.strftime('%H:%M:%S'))