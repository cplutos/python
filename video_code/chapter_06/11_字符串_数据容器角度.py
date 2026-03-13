 # 字符串下标
msg = 'welcome to atguigu'

print(msg[3])
print(msg[-1])

# 字符串中的字符，不可修改
msg = 'welcome to atguigu'
# msg[1] = 'a'

# 字符串不能嵌套
msg  = 'welcome to "hello" atguigu'
print(msg[11])

# 常用方法
# index
msg = 'welcome to atguigu'
print(msg.index('e'))

# split方法
msg = 'welcome to atguigu'
result = msg.split('e')
print(result)

# replace方法
msg = 'welcome to atguigu'
result = msg.replace('e','E')
print(result)

# replace方法
msg = 'welcome to atguigu'
result = msg.count('e')
print(result)

#   strip方法：从某个字符串中删除指定字符串中的任意字符，规则：从字符串两端开始删除，直到第一个不在指定字符串中的字符就停下。
msg = '666爱6学6习666'
result = msg.strip('6')
print(result)

msg = '1234爱12学34习4321'
result = msg.strip('1234')
print(result)


msg = '1234爱12学34习12534'
result = msg.strip('2143')
print(result)


msg = '  爱学习   '
result = msg.strip()
print(msg)
print(result)

# 常用内置函数
msg = '  爱学习   '
print(len(msg))

# 遍历
index = 0
while index<len(msg):
    print(msg[index])
    index+=1

for item in msg:
    print(item)