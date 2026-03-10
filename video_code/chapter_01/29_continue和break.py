# 测试 continue
for day in range(1,5):
    print(f'-----第{day}天-----')
    print("吃饭")
    if day == 2:
        continue
    print("睡觉")

# 测试break
for d in range(1,5):
    print(f'-----第{d}天-----')
    print('吃饭')
    for i in range(1,3):
        print(f'牛奶{i}')
        print(f'面包{i}')
        if i == 2:
            break
        print(f'油条{i}')
    print()
