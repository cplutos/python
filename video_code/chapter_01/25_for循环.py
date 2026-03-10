n = 0
for n in range(0,10):
    print(f'第{n}次你好啊')
print(f'我是for循环以外的代码，执行到这里时，循环结束，此时的n是：{n}')

for m in 'abcdefg':
    print(m)

nums = [1,2,3]
for i in nums:
    # 死循环，始终在列表最后一位添加4
    # nums.append(4)
    print(i)