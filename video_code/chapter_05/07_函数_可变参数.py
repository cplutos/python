 # 定义函数
def test1(*args):
    print(args)
test1('张三','男',18,124)


 # 定义函数
def test2(**kwargs):
    print(kwargs)
test2(name='张三',gender='男',age=18,heigh=124)

 # 定义函数
def test3(*args,**kwargs):
    print("1222222222222222222222222")
    print(args)
    print(kwargs)
test3('张三','男',name='张三',gender='男',age=18,heigh=124)