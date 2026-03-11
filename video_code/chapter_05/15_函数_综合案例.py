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

def main(title , duration):
    print(f'【{title}】【{duration}】天挑战赛，请输入每天的数量')
    num1 = int(input('第1天：'))
    num2 = int(input('第2天：'))
    num3 = int(input('第3天：'))
    num4 = int(input('第4天：'))
    num5 = int(input('第5天：'))
    num6 = int(input('第6天：'))
    num7 = int(input('第7天：'))
    num8 = int(input('第8天：'))

    total = calc_total(num1,num2,num3,num4,num5,num6,num7,num8)

    avg = calc_avg(total,duration)

    result = check_result(total)

    print(f'总数{total}，平均数{avg}，结果：{result}')

main('俯卧撑',8)

