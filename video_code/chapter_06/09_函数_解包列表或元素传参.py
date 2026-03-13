# def test(data):
#     print(f'我是test函数，我收到的参数是：{data}')
#
# list1 = [100,200,300,400]
# tuple1 = ('a','b','c','d')
# # 函数调用时，正常传递：列表或元组
# test(list1)
# test(tuple1)

# 定义函数时，使用*args（变量可一定非要用args，可以 *任意字符）将收到的多个参数打包成一个元组
def test(*args):
    print(f'我是test函数，我收到的参数是：{args}')

list1 = [100,200,300,400]
tuple1 = ('a','b','c','d')
# 函数调用时，使用*对：列表或者元组进行解包后，在传递参数
test(*list1) # 此种写法相当于test(100,200,300,400)
test(*tuple1)# 此种写法相当于test('a','b','c','d')