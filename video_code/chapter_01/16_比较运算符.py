# python中字符串进行比较式，是一次比较每个字符的Unicode编码，只要某一位分出大小就不必后续，内容比完比长度，越长越大
# 注意：Unicode编码不是Python特有的，而是全世界的标准
# 使用ord()函数查看Unicode，使用chr()将Unicode转字符
msg1 = 'abc'
msg2 = 'xyz'
msg3 = '我爱你'
msg4 = '中国'
print(msg1 > msg2)
print(msg3>msg4)
print(ord('我'))
print(ord('中'))
print(chr(43))
print(chr(3))

