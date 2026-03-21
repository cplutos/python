# 1. 概述：
#   a. 在Python中，一个.py文件就是一个模块（Module）
#   b. 模块中可以包含：变量、函数、类等很多内容
#   c. 通常把能够实现某一特定功能的代码，集中放在一个模块中（模块就类似于一个工具箱）。
#   d. 模块可以提高代码的可维护性 与 复用性，可以避免命名冲突。
# 2. 模块的分类：标准库模块、自定义模块、第三方模块
# 3. 模块命名注意点：
#   a. 要符合命名规范
#   b. 模块名区分大小写
#   c. 不要与标准库模块同名（一旦同名，Python会优先引入标准库模块）

# 4. 常见的模块导入方式
# a. import 模块名
# import order
# import pay
#
# print(order.max_order_amount)
# order.create_order()
# order.cancel_order()
# order.show_info()
#
# print(pay.timeout)
# pay.wechat_pay()
# pay.ali_pay()
# pay.show_info()

# b. import 模块名 as 别名
# import order as dd
# import pay as zs
#
# print(dd.max_order_amount)
# dd.create_order()
# dd.cancel_order()
# dd.show_info()
#
# print(zs.timeout)
# zs.wechat_pay()
# zs.ali_pay()
# zs.show_info()

# c. from 模块名 import 具体内容1，具体内容2，。。。
# from order import max_order_amount,show_info
# from pay import ali_pay,wechat_pay
#
# print(max_order_amount)
# show_info()
# ali_pay()
# wechat_pay()

# d. from 模块名 import 具体内容1 as 别名1，具体内容2 as 别名2，。。。
# from order import max_order_amount,show_info as show1
# from pay import ali_pay,wechat_pay,show_info as show2
#
# print(max_order_amount)
# show1()
# show2()
# ali_pay()
# wechat_pay()

# e. from 模块名 import *
# from order import *
# from pay import *
#
# max_order_amount = 10
#
# print(max_order_amount)
#
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()

# 关于__all__:
# 在Python中，可以通过 __all__ 来控制【from 模块 import *】 能导入哪些内容。
# __all__的值可以是：元组、列表
# from  order import max_order_amount
# print(max_order_amount)

# 关于__name__:
# __name__是每个Python模块都拥有的一个内置变量。
# 他的具体值取决于模块的允许方式
# 1.作为主程序直接运行,__name__的值是__main__
# 2.作为模块被导入到其他程序中运行,__name__的模块文件名(不带.py)
import pay
