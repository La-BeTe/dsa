def are_there_duplicates(*args):
    left, right = 0, 1
    while left < len(args) - 1:
        if args[left] == args[right]:
            return True
        else:
            right += 1
        if right == len(args):
            left += 1
            right = left + 1
    return False

print(are_there_duplicates(1, 2, 3))
print(are_there_duplicates(1, 2, 2))
print(are_there_duplicates(1, 2, 3, 1))