# 定义：给变量加上类型说明，可增强代码的可读性，让IDE的提示更友好
num: int = 100
price: float = 10.2
message: str = '100'
is_vip: bool = True
result: None = None  # 语法上没有问题，但没有实际意义

# 注意：可以先写变的类型注解，以后再赋值
school: str
print('*****')
school = '你好'

# hobby 是列表，并且列表中的所有元素必须是str类型
hobby: list[str] = ['a', 'b', 'c']
print(hobby)
# hobby 是列表，并且列表中的 元素可以是int或者str类型
hobby: list[str | int] = ['a', 'b', 'c']
# 上面这行代码的旧版本写法如下
from typing import Union

hobby: list[Union[str, int]] = ['a', 'b', 'c']

# citys 是集合，并且集合中所有元素必须是str类型
citys: set[str] = {'北京', '上海', '深圳'}

# citys 是集合，并且集合中元素可以是str或float或int类型
citys: set[str | int | float] = {'北京', '上海', '深圳'}

# persons 是字典，键是str类型，值是int类型
persons: dict[str, int] = {'张三': 3, '李四': 4}
# persons 是字典，键是str类型，值是int或str类型
persons: dict[str | int, str] = {'张三': 3, '李四': 4}

# 元组的声明有点特殊，需要注意
# scores 是元组，并且元组中仅包含1个int类型元素
scores: tuple[int] =(1,)

# scores 是元组，并且元组中仅包含3个int类型元素
scores: tuple[int,int,int] =(1,2,3)

# scores 是元组，并且元组中包含任意个int类型元素
scores: tuple[int,...] =(1,2,3,199,2,2,5)

# scores 是元组，并且元组中包含任意个int或者str类型元素
scores: tuple[int|str,...] =(1,2,3,199,2,2,5)

# Python会根据初始赋值推导变量的类型：
# 1.对于普通变量：后续如果改变类型，不会警告
# 2.对于容器变量：要求内容元素类型必须与推导出来的一致，否则就会被警告
x = 100
x = '你好'

