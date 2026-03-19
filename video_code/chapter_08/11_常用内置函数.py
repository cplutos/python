# 一、输入与输出
# print() ===>输出指定内容
# 完成参数：print(*objects,sep='',end = '\n',file = sys.about, flush = False)
# 参数详解：
# 1. objects：要输出的内容
# 2. sep：分隔符
# 3. end：结束符
# 4. file：输出位置
# 5. flush：是否立即刷新

f = open('a.text','w',encoding='utf-8')
print(10,20,30,40,sep='-',end='!',file=f)

# 第一种进度条
import time
# print('加载中',end='')
# for index in range(5):
#     print('.',end='',flush=True)
#     time.sleep(1)
# print('完成！',end='')

# 第二种进度条
# for index in range(1,101):
#     print(f'\r已加载{index}%',end='',flush=True)
#     time.sleep(0.1)

# input() 输入

# 二、类型转换
str()
int()
list()
tuple()
set()
dict()

# 三、数学相关
# abs() 取绝对值
# round() -->四舍五入 ：银行家算法，大于5就入，小于于五就舍弃，等于五看奇偶（奇入偶舍）
# print(round(1.2))
# print(round(2.5))
# print(round(3.5))
# print(round(4.5))
# print(round(5.532),2)
# print(round(6.532))
# pow（值，幂，取余值） 求次方
# print(pow(2, 3, 3))  # 2^3  % 3

# divmod()  商和余数
# print(divmod(10,3))
# max()
# min()
# sum() 求和
# map() 加工数据
# filter() 过滤数据
# reduce() 合并计算
# sorted() 排序

# 四、数据容器相关
# len() 容器元素个数
# range(起始索引，索引长度，步长) 生成数字序列
for index in range(0,10,2):
    print(index)
# sorted() 排序
# enumerate() 给序列添加索引
# zip() 将多个序列一一配对,组成元组
name = ('a','b','c')
nums = [1,2,3]
x = zip(name,nums)
print(list(x))

# 五、类型判断与对象相关
# type()  看类型
# isinstance() 判断类型
# issubclass() 判断两个类型的继承关系
# id()    查看对象的内存地址

# 六、逻辑判断相关
# all()  全真返回True
# any()   有一个为真即可
l1 = ['10','sd',0,{1,2}]
print(all(l1))

l2 = []

# 七、字符串辅助相关
# ord()     获取字符的Unicode
# chr()     将Unicode编码转为字符



