
def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


l = [5, 3, 6, 2, 10, 9, 8, 4, 7, 1]
print(quick_sort(l))

# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
