class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = 0
        start = 0
        longest_substr_length = 0
        current_substr_length = 0
        hash_map = {}
        str_len = len(s)
        while start < str_len and (str_len - start) > longest_substr_length:
            if current >= str_len or s[current] in hash_map:
                start += 1
                current = start
                longest_substr_length = max(longest_substr_length, current_substr_length)
                current_substr_length = 0
                hash_map = {}
            else:
                hash_map[s[current]] = 1
                current_substr_length += 1
                current += 1
        return longest_substr_length
        