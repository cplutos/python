# 0b开头表示二进制
num1 = 0b1011
# 0o开头表示八进制
num2 = 0o1032
# 0x开头表示十六进制
num3 = 0x1cf

print(num1,num2,num3)

# 进制转换十进制转字符串
result1 = bin(19)
result2 = oct(19)
result3 = hex(19)
print(result1,result2,result3)
print(type(result1),type(result2),type(result3))

# int()将指定进制的数转为十进制
value1 = int('0b1011',2)
value2 = int('0o1077',8)
value3 = int('0x2daf',16)

print(value1,value2,value3)



