def greet(name,gender,age,height):
    print(f'我叫：{name},性别{gender},年龄是{age}，身高{height}cm')

# 调用
greet('张三','男',13,120)
# 错误
# greet('张三',13,120)
# greet('男','张三',13,120)