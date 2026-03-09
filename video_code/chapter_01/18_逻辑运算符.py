# and用于判断两值是否都为True
print(True and False)
print(True and True)
print(False and False)

# and 具备逻辑短路能力
print(False and 3 / 0)
# print(True and 3/0)

# and返回的不一定是布尔值，他返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后在进行逻辑操作
print(2 - 2 and True)
print('' and True)
print(True and 8 / 2)
print(3 + 3 and 3 * 4)

# or也具备逻辑短路的能力
# or返回的不一定是布尔值，他返回的是某个参与计算的值本身
# 规则：or会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那Python会自动转为布尔值，然后在进行逻辑操作
print(7-2 or False)
print('你好' or '尚硅谷')
print(False or 8/2)
print(3 + 3 or 3 * 4)

# not用于取反
# 备注：若参与or运算的值不是布尔值，那Python会自动转为布尔值，然后在进行逻辑操作
# not返回的值，一定是布尔值
print(not 0)
print(not 3>2)
print(not 9//4)
print(not 2*4)