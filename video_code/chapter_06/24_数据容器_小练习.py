# 练习一：水果清单
fruits = {
    '苹果': 3.5,
    '香蕉': 2.1,
    '葡萄': 5.5,
    '草莓': 9.6
}
# 打印所有水果
# for item in fruits:
#     print(f'{item}的价格是：{fruits[item]}')

# 找最贵的水果
# key = max(fruits, key=fruits.get)
# print(f'最贵的水果是{key}，价格是：{fruits[key]}')

students = [
    {
        "name": '张三',
        'scores': {'语文': 78, '数学': 80, '英语': 96}
    },
    {
        "name": '李四',
        'scores': {'语文': 85, '数学': 74, '英语': 22}
    },
    {
        "name": '王五',
        'scores': {'语文': 34, '数学': 85, '英语': 77}
    }
]
# 求每个学生的最高分
# for stu in students:
#     score_list = stu['scores'].values()
#     avg = sum(score_list) / len(score_list)
#     print(f'{stu["name"]}的平均成绩是：{avg:.1f}')

# 找到总分最高的学生
def find_best():
    best_score = 0
    best_students = []

    for stu in students:
        total = sum(stu['scores'].values())
        if total > best_score:
            best_students = [stu['name']]
            best_score = total
        elif total == best_score:
            best_students.append(stu['name'])
    print(f'最高分为{best_score},是{best_students}')
find_best()