class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_length = 0
        for j, char in enumerate(s):
            while char in s[i:j]:
                i = i + 1
            max_length = max(max_length, j - i + 1)
        return max_length