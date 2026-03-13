print('请输入学生成绩，输入“结束”停止录入')
score_list = []

while True:
    data = input("请输入成绩：")
    if data == '结束':
        break
    else :
        score_list.append(int(data))

if score_list:
    avg = sum(score_list) / len(score_list)
    pass_count = 0
    excellent_count = 0
    for item in score_list:
        if item>60:
            pass_count+=1
        elif item>90:
            excellent_count+=1
    pass_rate = pass_count / len(score_list)
    excellent_rate = excellent_count / len(score_list)

print("统计信息如下：")
print(f'总人数为：{len(score_list)}')
print(f'最高分为：{max(score_list)}')
print(f'最低分为：{min(score_list)}')
print(f'平均分为：{avg}')
print(f'最高分为：{max(score_list)}')

