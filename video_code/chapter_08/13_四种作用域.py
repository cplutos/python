a = 100

def test(b):
    # *********外层函数作用域
    print('我是test函数')
    print('test中打印的a是：',a)
    print('test中打印的b是：', b)
    c = 200
    d = 300
    print('test中的c和d是：',c,d)
    def inner():
        e = 600
        nonlocal c
        c = 999
        print('inner中的e是：',e)
        print('inner中的a,b,c是:',a,b,c)
    inner()
    print(c)

print('全局打印的a是：',a)
test(66)