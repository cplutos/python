nums = [10, 23, 54, 75, 23]

nums.append(2)
print(nums)
nums.insert(2, 90)
print(nums)

# nums.extend('d')
nums.extend(range(1,3))
nums.extend(['a','b','c'])
print(nums)


# 删除
# 方式一 pop删除指定下标元素

# nums1 = [10, 23, 54, 75, 23]
# result = nums1.pop(1)
# print(result,nums1)

# 方式二 remove删除第一次出现的值
nums1 = [10, 23, 54, 75, 10]
nums1.remove(10)
print(nums1)

# 方式三 del 指定列表下标的值
nums1 = [10, 23, 54, 75, 10]
del nums1[1]
print(nums1)

# 修改
nums1 = [10, 23, 54, 75, 10]
nums1[0] = 1
print(nums1)

# 查询
nums1 = [10, 23, 54, 75, 10]
print(nums1[3])