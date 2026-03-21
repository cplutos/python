# 1. 概述：
#   a. 在Python中，【包含__init__.py的文件夹】就是一个包【package】
#   b. 我们通常会把【某个特定功能相关的所有模块】放入一个包中
#   c. 使用包可以进一步提高代码的：可维护性、可复用性、便于管理大项目
# 2. 包与模块的关系：
#   a. 一个模块就是一个.py文件，包是用来‘管理模块’的目录（文件夹）
#   b. 一个包中可以有多个慕课，也可以有多个自爆
# 3. 包的分类：
#   a. Python中的包分为三类，分别是：标准库包、自定义包、第三方包
# 4. 包命名的注意点：
#   a. 要符合标识符的命名规范
#   b. 报名区分大小写（建议全部使用小写字母）
#   c. 不要和标准库包同名
from tkinter.font import names

# a. import 包名.模块名
# import trade.order
# import trade.pay
# trade.order.create_order()
# trade.pay.wechat_pay()

# b. import 包名.模块名 as 别名
# import trade.order as zz
# import trade.pay as df
# zz.create_order()
# df.wechat_pay()

# c. from 包名.模块名 import 具体内容1，具体内容2，。。。
# from trade.order import max_order_amount,create_order
# from trade.pay import timeout,wechat_pay
# print(max_order_amount)
# print(timeout)
# create_order()
# wechat_pay()

# d. from 包名.模块名 import 具体内容1 as 别名1，具体内容2 as 别名2，。。。
# from trade.order import max_order_amount as mx,create_order as co
# from trade.pay import timeout as t,wechat_pay as wp
# print(mx)
# print(t)
# co()
# wp()
# e. from 包名.模块名 import *
# from trade.order import *
# from trade.pay import *
#
# print(max_order_amount)
# create_order()
# cancel_order()
#
# print(timeout)
# wechat_pay()
# ali_pay()

# f. from 包名 import 模块名
from trade import order as dd,pay as p
dd.create_order()
p.wechat_pay()

# 关于__init__.py文件：
# 1.__init__.py 是包的初始化文件，在包被导入是，__init__.py会被自动调用
# 2.__init__.py 中是可以编写一些包的初始化逻辑
# 3.__init__.py 中定义的内容，会被【from 包名 import *】的形式全部引入
# 4.__init__.py 中也可以使用__all__ 来控制包中的哪些模块可以被【from 包名 import *】 引入

# g. from 报名 import *
from trade import  *

# print(a)
# print(b)
print(order.max_order_amount)
order.create_order()
print(pay.timeout)
pay.wechat_pay()

# h. import 包名
import trade
print(trade.a)
print(trade.b)
trade.order.create_order()
trade.pay.show_info()

# 测试一下引入子包
# from trade.hello.h1 import say_hello
# say_hello()

# 演示标准库包的使用
from collections import Counter
names = ['a','b','c','d','a']
result = Counter(names)
print(result)