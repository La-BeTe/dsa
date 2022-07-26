def is_subsequence(s1, s2):
    i = j = 0
    while j < len(s2):
        if i < len(s1) and s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)

print(is_subsequence('abc', 'acb')) # False
print(is_subsequence('sing', 'string')) # True
print(is_subsequence('abc', 'abracadabra')) # True
print(is_subsequence('hello', 'hello world')) # True