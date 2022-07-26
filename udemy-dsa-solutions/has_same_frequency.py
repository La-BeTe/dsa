def has_same_frequency(num1, num2):
    hash_map = {}
    while num1 > 0:
        digit = num1 % 10
        hash_map[digit] = (0 if digit not in hash_map else hash_map[digit]) + 1
        num1 = int(num1 / 10)
    while num2 > 0:
        digit = num2 % 10
        if digit not in hash_map or hash_map[digit] < 1:
            return False
        hash_map[digit] -= 1
        num2 = int(num2 / 10)
    return True

print(has_same_frequency(34, 14))
print(has_same_frequency(222, 222))
print(has_same_frequency(281, 182))