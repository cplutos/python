def greet(name, gender, age, height, msg='你好'):
    """
    组装函数
    :param name: 姓名
    :param gender: 性别
    :param age: 年龄
    :param height: 身高
    :param msg: 消息
    :return: 无
    """
    print(f'我叫：{name},性别{gender},年龄是{age}，身高{height}cm')
    print(f'我想说{msg}')


# 调用
greet('张三', '男', age=13, height=120)
greet(age=13, name='张三', gender='男', height=120, msg='靓仔还在学')
