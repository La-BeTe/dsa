def flatten(li):
    result = []
    for item in li:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, 2, 3, [4, 5] ])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1],[2],[3]])) # [1,2,3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1,2,3]