score_list = [12,35,57,2,57,2,4]
# while循环
index = 0
while index < len(score_list):
    print(score_list[index])
    index+=1

# for循环
# 写法一
print('写法一：')
for item in score_list:
    print(item)
# 写法二
print('写法二：')
for i in range(len(score_list)):
    print(score_list[i])
# 写法三 start参数仅修改编号，不修改索引值
print('写法三：')
for index,j in enumerate(score_list):
    print(index,j)
print('加start参数')
for index,j in enumerate(score_list,start=5):
    print(index,j,score_list[0])
print(score_list[0])