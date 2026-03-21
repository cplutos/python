# 1.为什么
# 程序运行过程中出现的异常，如果得不到处理，那程序就会立即崩溃，导致后续代码无法执行。
# 异常不是让程序消失，而是将异常捕获到，随后根据异常的具体情况，来执行指定的逻辑。

# 2. 异常处理（初级）：
#   a. 将可能出现的代码放在try中，出现异常后的处理代码写在except中
#   b. 如果try中的代码出现异常，那try中的后续代码将不会执行，并自动跳转到except中处理异常
#   c. 如果try中的代码没有异常，那except中的代码不会执行
# print('欢迎')
# try:
#     a=int(input('number1:'))
#     b = int(input('number2:'))
#     result = a/b
#     print(f'{a}除以{b}的结果是:{result}')
# except:
#     print('出现了异常')
# print('其他逻辑1')
# print('其他逻辑2')

# 3.异常处理：捕获指定类型的异常
# print('欢迎')
# try:
#     a=int(input('number1:'))
#     b = int(input('number2:'))
#     result = a/b
#     print(f'{a}除以{b}的结果是:{result}')
# except ZeroDivisionError:
#     print('出现了异常,O不能为除数')
# except ValueError:
#     print('出现异常，必须为数字')
# print('其他逻辑1')
# print('其他逻辑2')

# 4.验证一下异常类之间的关系
print(issubclass(ZeroDivisionError,ArithmeticError))
print(issubclass(ValueError,Exception))

# 5.多个except从上往下匹配吗，匹配成功后不再向下匹配
# print('欢迎')
# try:
#     a=int(input('number1:'))
#     b = int(input('number2:'))
#     result = a/b
#     print(f'{a}除以{b}的结果是:{result}')
# except Exception:
#     print('程序异常')
# except ZeroDivisionError:
#     print('出现了异常,O不能为除数')
# except ValueError:
#     print('出现异常，必须为数字')
# print('其他逻辑1')
# print('其他逻辑2')

# 6.获取异常的具体信息
# print('欢迎')
# try:
#     a=int(input('number1:'))
#     b = int(input('number2:'))
#     print(x)
#     result = a/b
#     print(f'{a}除以{b}的结果是:{result}')
#
# except ZeroDivisionError:
#     print('出现了异常,O不能为除数')
# except ValueError:
#     print('出现异常，必须为数字')
# except Exception as e:
#     # print(f'程序异常,内容为：{e}')
#     # print(f'异常类型：{type(e)}')
#     # print(f'异常参数：{e.args}')
#     # print(f'异常文件：{e.__traceback__.tb_frame.f_code.co_filename}')
#     # print(f'异常的具体行数为：{e.__traceback__.tb_lineno}')
#     # 通过traceback来回溯异常
#     import traceback
#     print(traceback.format_exc())
# print('其他逻辑1')
# print('其他逻辑2')

# 7.一个except，也可以捕获不同的异常
print('欢迎')
try:
    a=int(input('number1:'))
    b = int(input('number2:'))
    result = a/b
    print(f'{a}除以{b}的结果是:{result}')
except(ZeroDivisionError,ValueError,Exception) as e:
    if isinstance(e,ZeroDivisionError):
        print('出现了异常,O不能为除数')
    elif isinstance(e,ValueError):
        print('出现异常，必须为数字')
    else:
        print(f'程序异常,内容为：{e}')
# except ZeroDivisionError:
#     print('出现了异常,O不能为除数')
# except ValueError:
#     print('出现异常，必须为数字')
# except Exception as e:
#     print(f'程序异常,内容为：{e}')
print('其他逻辑1')
print('其他逻辑2')

# 8.异常处理的完整写法：
# 1.try：尝试去做可能会出现异常的事情
# 2.except：出现异常时的处理
# 3.else：如果一切顺利要做的事情
# 4.finally：无论有没有异常，都要做的事情

print('欢迎')
try:
    a=int(input('number1:'))
    b = int(input('number2:'))
    result = a/b
    print(f'{a}除以{b}的结果是:{result}')
except(ZeroDivisionError,ValueError,Exception) as e:
    if isinstance(e,ZeroDivisionError):
        print('出现了异常,O不能为除数')
    elif isinstance(e,ValueError):
        print('出现异常，必须为数字')
    else:
        print(f'程序异常,内容为：{e}')
else:
    print('try中没有任何异常')
finally:
    print('无论有没有异常，我的计算都结算了')
print('其他逻辑1')
print('其他逻辑2')