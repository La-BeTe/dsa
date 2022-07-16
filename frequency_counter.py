def compare_lists(l1, l2):
    if len(l1) != len(l2):
        return False
    
    hash_map = {}
    for num in l1:
        num_squared = num ** 2
        hash_map[num_squared] = 1 if num_squared not in hash_map else hash_map[num_squared] + 1

    for num in l2:
        if num not in hash_map or hash_map[num] < 1:
            return False
        hash_map[num] -= 1
    return True

print('-----compare_lists-----')
print(compare_lists([1, 2, 3], [1, 9]))
print(compare_lists([1, 2, 3], [4, 1, 9]))
print(compare_lists([1, 2, 1], [4, 1, 4]))
print(compare_lists([1, 2, 3, 2, 5], [9, 1, 4, 4, 11]))
        
def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    hash_map = {}
    for char in s1:
        hash_map[char] = (0 if char not in hash_map else hash_map[char]) + 1
    
    for char in s2:
        if char not in hash_map or hash_map[char] < 1:
            return False
        hash_map[char] -= 1
    return True

print('------check_anagram------')
print(check_anagram('', ''))
print(check_anagram('rat', 'car'))
print(check_anagram('qwerty', 'qtwyre'))
print(check_anagram('anagram', 'nagaram'))