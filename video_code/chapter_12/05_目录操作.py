import os
import shutil

# 创建目录
# os.mkdir('demo/a')

# 创建多级目录
# os.mkdir('demo/a/b')

# 删除空目录
# os.rmdir('demo/a/b')

# 递归删除空目录
# os.removedirs('demo/a')

# 判断目录是否存在
# r = os.path.exists('demo')
# print(r)

# 判断路径os.path.isdir(path)
# 不存在 False
# 路径存在，但指向的是文件 False
# 路劲存在，并且是目录  True
# r = os.path.isdir('demo.txt')
# print(r)

# 扫描指定目录
# res = os.scandir('../chapter_12')
# print(res)
# for item in res:
#     print('目录' if item.is_dir() else '文件',item.name)

# 按层级递归遍历指定目录
# res = os.walk('../chapter_12')
# print(res)
# for item in res:
#     print(item)

# 删除有内容的目录
shutil.rmtree('demo')