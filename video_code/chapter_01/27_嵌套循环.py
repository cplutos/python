from lib2to3.pgen2.tokenize import group

for i in range(1,31):
    print(f"********第{i}天********")
    for j in range(1,4):
        print(f"这是第{j}组俯卧撑")
    print(f'第{i}天任务已完成\n')
print('训练已完成，腹肌闪闪发光！')

day = 1
while day<=30:
    print(f"********第{day}天********")
    group = 1
    while group<=4:
        print(f"这是第{group}组俯卧撑")
        group+=1
    print(f'第{day}天任务已完成\n')
    day+=1
print('训练已完成，腹肌闪闪发光！')
