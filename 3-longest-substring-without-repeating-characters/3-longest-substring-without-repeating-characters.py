class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest_substr_length = 0
        current_substr_length = 0
        hash_map = {}
        while start < len(s):
            if end < len(s) and s[end] not in hash_map:
                hash_map[s[end]] = 1
                end += 1
                current_substr_length += 1
            else:
                start += 1
                end = start
                longest_substr_length = max(longest_substr_length, current_substr_length)
                current_substr_length = 0
                hash_map = {}
        return longest_substr_length
        