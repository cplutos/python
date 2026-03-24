# open 函数最常用的三个参数如下：
# 1、file：要操作的文件路径
# 2.mode：文件的打开模式
#     r：读写
#     w：写入，先截断文件（清空）
#     x：排他性创建，如果文件已存在，则创建失败
#     a：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#     b：二进制模式
#     t：文本模式
#     +：打开用于更新（读取与写入）
# 3.encoding：字符编码
import time
# w模式
# with open('a.txt','wt',encoding='utf-8') as file:
#     file.write('你好')
#
# x模式
# with open('a.txt','xt',encoding='utf-8') as file:
#     file.write('你好')

# a模式
# with open('a.txt', 'at', encoding='utf-8') as file:
#     file.write('你好')
# Python中文件写入是，并不是没写一次就立即落盘，而是先进缓冲区
# 文件对象的 flush 方法：把缓冲区中的数据，立即写入到文件中。
# with open('demo.txt', 'at', encoding='utf-8') as file:
#     file.write('你好1')
#     file.write('你好2')
#     file.flush()
#     time.sleep(20)
#     file.write('你好3')
#     file.write('你好4')


# 测试rt+
# with open('a.txt', 'rt+', encoding='utf-8') as file:
#     # seek(offset,whence)方法：用于改变文件对象指针的位置，参数说明如下：
#     # offset：偏移量，要移动多少距离
#     # whence：参考点，从哪里开始计算偏移，有三种取值：
#     # 0：从文件开头计算
#     # 1：从当前位置计算
#     # 2：从文件末尾计算
#     file.seek(3,0)
#     file.write('你好')

# 测试wt+
# with open('a.txt', 'wt+', encoding='utf-8') as file:
#     file.write('你好')
#     file.seek(0,0)
#     result = file.read()
#     print(result)
