"""
所谓整型，就是没有小数点的数字， 可以是正数，也可以是负数，也可以是0
当数字很大是可以使用下划线将数字进行分组，让数字更容易读懂
Python中整数的上限值，取决于执行代码计算机的内存和处理能力
"""
import sys

salary = 2000_000
house_price = 1_000_000


a = 9 ** 9999
# b = a + 100
sys.set_int_max_str_digits(0)
print(a)