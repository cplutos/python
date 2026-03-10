def greet(name,/,gender,*,age,height):
    print(f'我叫：{name},性别{gender},年龄是{age}，身高{height}cm')

# 调用
greet('张三',gender='男',age = 13, height=120)
# greet(age = 13,name='张三',gender='男', height=120)
# greet(name='张三','男',age = 13, height=120)
