from math import inf


def min_sublist_len(l1, num):
    left = 0
    min_len = inf
    while left < len(l1):
        current_sum = 0
        ptr = left
        while True:
            current_sum += l1[ptr]
            if current_sum >= num:
                min_len = min(min_len, ptr - left + 1)
                break

            ptr += 1
            if ptr >= len(l1):
                # If current_sum still less than num by now,
                # just end the outer while loop as there's no way to sum up to num
                # with the list passed in
                left = len(l1)
                break
        left += 1
    return min_len if min_len != inf else 0

print(min_sublist_len([2, 3, 1, 2, 4, 3], 7)) # 2
print(min_sublist_len([4, 3, 3, 8, 1, 2, 3], 11)) # 2
print(min_sublist_len([1,4,16,22,5,7,8,9,10],95)) # 0
print(min_sublist_len([1,4, 16,22,5,7,8,9,10],55)) # 5
print(min_sublist_len([1,4, 16, 22,5,7,8,9,10],39)) # 3
print(min_sublist_len([3,1,7, 11,2, 9, 8, 21, 62, 33, 19], 52)) # 1

