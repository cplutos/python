# 当程序遇到不符合预期情况时，可以使用raise 语句手动触发（抛出）异常
print('判断年龄')
try:
    age = int(input('输入年龄：'))
    if 18 <=age <=120:
        print('成年')
    elif 0<=age<18:
        print('未成年')
    else:
        # print('输入错误')
        raise ValueError('输入不在正常范围')
except Exception as e:
    print(f'出现异常：{e}')

raise NameError('dsuiafhiuhasdfiu')
