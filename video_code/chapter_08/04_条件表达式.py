# 表达式：执行后能得到值的代码，就是表达式（表达式最终会形成一个值，可以写在任何需要值的地方）
a1 = 3+6
a2 = 'abc'*3
print(5>4)
print('y' in 'python')
a6 = len('hello')

# 条件表达式：根据条件的真假，在两个结果中二选一的表达式（又称三元表达式，三目运算符）
age = 16
# 传统写法
if age>=18:
    text= '成年'
else:
    text = '未成年'
# 条件表达式
text = '成年' if age>= 18 else '未成年'
print(text)
# 使用场景：常规二选一
rain = True
eat = '外卖' if rain else '出去吃'

is_vip = True
discount = 0.8 if is_vip else 1.0

is_login=False
msg = '欢迎回来' if is_login else print('哈哈哈')

print(eat)
print(discount)
print(msg)