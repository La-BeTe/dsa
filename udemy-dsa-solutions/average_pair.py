def average_pair(l1, average):
    sum_to_search_for = average * 2
    left, right = 0, len(l1) -1
    while left < right:
        sum_of_left_and_right = l1[left] + l1[right]
        if sum_of_left_and_right == sum_to_search_for:
            return True
        elif sum_of_left_and_right < sum_to_search_for:
            left += 1
        else:
            right -= 1
    return False

print(average_pair([], 4)) # False
print(average_pair([1, 2, 3], 2.5)) # True
print(average_pair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8)) # True
