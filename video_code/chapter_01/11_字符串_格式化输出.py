"""
文本穿插字符输出格式
"""
name = '张三'
gender = '男'
weight = 76.3
age = 14

# 写法一：直接用加号进行拼接,写起来麻烦且代码乱，而且只能是字符串之间的拼接
info1 = '我叫' + name + ',我是' + gender + '生'
print(info1)

# 写法二：使用占位符
info2 = "我叫%s，我是%s生,我的体重是%.2f，年龄是%i" % (name, gender, weight, age)
print(info2)

# 写法三：使用f-string
info3 = f'我叫{name}，我是{gender}生，我的体重是{weight},我的年龄是{age}'
print(info3)