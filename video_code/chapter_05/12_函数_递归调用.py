def welcome(n):
    # 倒序输出
    print(f'你好{n}')
    if n>1:
        welcome(n-1)

    # 下面这种写法涉及函数调用执行顺序知识，可以顺序输入
    # if n > 1:
    #     welcome(n - 1)
    # print(f'你好{n}')
welcome(5)