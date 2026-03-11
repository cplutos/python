a = 200
b = 10


def test():
    c = '你好'
    d = '靓仔'
    print(a)
    print(b)
    print(c)
    print(d)

test()
# print(c)
# print(d)

n = 100
def test3():
    global n
    n += 1
    print(f'我是test3中的函数打印的n：{n}')
test3()
test3()
test3()