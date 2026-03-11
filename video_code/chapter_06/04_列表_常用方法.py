# 1. index（值）：查找该值第一次出现的下标
fruits = ['香蕉','苹果','菠萝']
result = fruits.index('香蕉')
print(result)
# 2. count（值）：统计某个元素在列表中出现的次数
num1 = [1,2,3,4,5,3]
result2 = num1.count(3)
print(result2)
# 3. reverse（）：反转列表
num2 = [1,2,3,4,5,3]
num2.reverse()
print(num2)
# 4. sort（reverse=布尔值）：对列表排序（从小到大，会改变原列表）
# 4.2 数字字符混搭时，排序会报错
# 4.3 如果都是字符串，按照Unicode大小排序
num3 = [1,2,3,4,5,3]
num3.sort(reverse=True)
print(num3)