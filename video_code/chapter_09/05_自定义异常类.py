# 自定义异常类
# 1. 由开发人员自己定义的一个异常类，用来表示代码中‘更具体、更有业务含义’的异常信息
# 2. 具体规则：定义一个类（类名通常以Error结尾），继承Exception 类或它的子类

class SchoolNameError(Exception):
    def __init__(self,msg):
        super().__init__('校名异常'+msg)

def check_school_name(name):
    if len(name)>10:
        raise SchoolNameError('学校名称过长')
    else:
        print('校名合法、')
try:
    check_school_name('adsifjoiasdjfioasdf')
except SchoolNameError as e:
    print(f'出现异常，内容：{e}')
