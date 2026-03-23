# Python中操作文件的标准流程：
# 1.创建【文件对象】
# 2.操作文件：读取，写入
# 3.关闭文件
#
# 文件操作核心：open函数：他可以打开或创建文件，且支持多种操作模式，返回值是【文件对象】。
# open 函数最常用的三个参数如下：
# 1、file：要操作的文件路径
# 2.mode：文件的打开模式
#     r：读写
#     w：写入
#     x：排他性创建，如果文件已存在，则创建失败
#     a：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#     b：二进制模式
#     t：文本模式
#     +：打开用于更新（读取与写入）
# 3.encoding：字符编码

# region Description
# # 读取操作 read
#
# # 创建文件对象
# # file = open(file='a.txt', mode='r', encoding='utf-8')
# # file = open('a.txt','r',encoding='utf-8')
# file = open('D:\\Workspace\\code-python\\python\\video_code\\chapter_12\\a.txt', mode='r', encoding='utf-8')
#
# # 读操作
# # r1 = file.read(2)
# # r2 = file.read(3)
# # r3 = file.read(4)
# # r4 = file.read(5)
# #
# # print(r1)
# # print(r2)
# # print(r3)
# # print(r4)
# # print(repr(r1))
# # print(repr(r2))
# # print(repr(r3))
# # print(repr(r4))
#
# # 用循环配合多次read
# while True:
#     result = file.read(10)
#     if result == '':
#         break
#     print(result,end='')
#
# # 关闭文件/释放资源
# file.close()
# endregion

# 读取操作2 readline

# region Description
# file = open('a.txt','r',encoding='utf-8')

# r1 = file.readline()
# r2 = file.readline()
# r3 = file.readline()
# r4 = file.readline()
#
# print(r1.strip())
# print(r2.strip())
# print(r3.strip())
# print(r4.strip())
# print(repr(r1))
# print(repr(r2))
# print(repr(r3))
# print(repr(r4))
#
# while True:
#     line = file.readline()
#     if line == '':
#         break
#     print(line.strip())
#
# file.close()
# endregion


# 读取操作3： for循环

# region Description
# file = open('a.txt','r',encoding='utf-8')
#
# for line in file:
#     print(line,end='')
# file.close()
# endregion

# 读取操作4：readlines 参数是最大字符个数
# region Description
# file = open('a.txt','r',encoding='utf-8')
#
# result = file.readlines()
# print(result)
#
# file.close()
# endregion

# 实践：使用with上下文管理，结合for循环遍历，逐行读取文件
with open('a.txt', 'rt',encoding='utf-8') as file:
    for line in file:
        print(line,end='')