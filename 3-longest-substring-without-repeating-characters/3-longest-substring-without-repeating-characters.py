class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_substr_length = 0
        while left < len(s):
            hash_map = {}
            ptr = left
            while s[ptr] not in hash_map:
                hash_map[s[ptr]] = 1
                ptr += 1
                if ptr == len(s):
                    break
            longest_substr_length = max(longest_substr_length, ptr - left)
            left += 1
        return longest_substr_length
            