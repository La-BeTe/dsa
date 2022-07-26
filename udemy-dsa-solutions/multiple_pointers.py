def sum_to_zero(l1):
    left = 0
    right = len(l1) -1
    while left < right:
        sum = l1[left] + l1[right]
        if sum > 0:
            right -= 1
        elif sum == 0:
            return [l1[left], l1[right]]
        else:
            left += 1
    return []
        

print(sum_to_zero([-102, -10, -3, 3, 4, 8, 100]))

def count_unique_values(l1):
    if len(l1) == 0:
        return 0
    left = 0
    right = 1
    num_of_unique_values = 1
    while left < len(l1):
        if len(l1) <= right:
            break
        if l1[left] != l1[right]:
            num_of_unique_values += 1
            left = right
        right += 1
    return num_of_unique_values
print(count_unique_values([]))
print(count_unique_values([-2, -1, -1, 0, 1]))
print(count_unique_values([1, 1, 1, 1, 1, 1, 2]))
print(count_unique_values([0, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5]))
