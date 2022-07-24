class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        hash_map = {}
        for i, char in enumerate(s):
            hash_map[char] = [] if char not in hash_map else hash_map[char]
            hash_map[char].append(i)
        start, end, longest_palindrome, longest_palindrome_len = 0, hash_map[s[0]][-1] + 1, '', 0
        hash_map_ptr = -1
        # print(hash_map['p'])
        while start < s_len:
            # print(start, end, longest_palindrome, hash_map_ptr)
            if longest_palindrome_len > (s_len - start):
                break
            if longest_palindrome_len > (end - start):
                start += 1
                hash_map_ptr = -1
                end = hash_map[s[start]][hash_map_ptr] + 1
                continue
            sliced_s = s[start:end]
            reversed_s = sliced_s[::-1]
            # print(sliced_s, reversed_s)
            if sliced_s == reversed_s:
                longest_palindrome = reversed_s
                longest_palindrome_len = len(reversed_s)
                start += 1
                hash_map_ptr = 0
            elif (len(hash_map[s[start]]) + hash_map_ptr) < 0:
                start += 1
                hash_map_ptr = 0
            if start >= s_len:
                break
            hash_map_ptr -= 1
            end = hash_map[s[start]][hash_map_ptr] + 1
        return longest_palindrome
                