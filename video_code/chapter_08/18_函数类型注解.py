# 给函数的【参数】和【返回值】添加类型说明
# 语法格式：函数名（参数1：类型，参数2：类型）——》返回值类型：。

# 实例1：设置参数类型注解、设置返回类型注解
# def add(x:int,y:int)->int:
#     return x+y


# 实例2：参数有默认值（Python可以推导出参数的类型）、设置返回值类型
def add(x=1,y=1) -> int:
    return  x+y

# 实例3：设置多个返回值的类型注解
def show_nums_info(nums: list[int])->tuple[int,int,float]:
    max_value = max(nums)
    min_value = min(nums)
    result = max_value/min_value
    return max_value,min_value,result

# 示例4：设置*args的类型注解，要求args中的每个参数都必须是int类型
def add(*args: int)-> int:
    return sum(args)

# 示例6：设置**kwargs 的类型注解，要求kwargs中的每组参数的值，必须是str或者int类型
def show_info(**kwargs: str|int) :
    print(kwargs)

# 获取函数的注解信息
print(add.__annotations__)