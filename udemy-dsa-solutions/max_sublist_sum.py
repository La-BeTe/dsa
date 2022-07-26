def max_sublist_sum(l1, num):
    if len(l1) < num:
        return None
    
    max_sum = 0
    for i in range(num):
        max_sum += l1[i]

    ptr = num
    while ptr < len(l1):
        new_sum = max_sum + l1[ptr] - l1[ptr - num]
        max_sum = max(new_sum, max_sum)
        ptr += 1
    
    return max_sum

print(max_sublist_sum([2, 3], 3)) # None
print(max_sublist_sum([-3, 4, 0, -2, -6, -1], 2)) # 5
print(max_sublist_sum([100, 200, 300, 400], 2)) # 700
print(max_sublist_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)) # 39