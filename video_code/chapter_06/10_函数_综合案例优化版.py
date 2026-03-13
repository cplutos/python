def calc_total(*nums):
    print(type(nums))
    print(sum(nums))
    return sum(nums)


def calc_avg(total, days=7):
    return total / days


def check_result(total, goal=120):
    if total >= goal:
        return '挑战成功'
    else:
        return '挑战失败'

def main(title , duration,goal):
    print(f'【{title}】【{duration}】天挑战赛，请输入每天的数量')
    nums = []
    for index in range(duration):
        nums.append(int(input(f"请输入第{index+1}天的数据")))


    total = calc_total(*nums)

    avg = calc_avg(total,duration)

    result = check_result(total,goal)

    print(f'总数{total}，平均数{avg}，结果：{result}')

main('俯卧撑',8,222)

