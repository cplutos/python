# 加密
test = input("请输入加密的文字：")
secret = ''
for t in test:
    unicode = chr(ord(t)+1)
    secret += unicode
print(f"加密后文本:{secret}")

# 解密
text = input('请输入需要解密的文字：')
answer = ''
for i in text:
    answer += chr(ord(i)-1)
print(f'解密后文本：{answer}')