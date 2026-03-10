# 1. None是一个特殊字面量，他表示：空值、无值、无意义
msg=None
# 2. None的类型是NoneType
print(type(msg))
# 3. None转为布尔值是False
print(bool(msg))
if not msg:
    print('你好')
# 4. None不能参与数学运算和字符串拼接
# print(msg+1)
# print(msg+"")