class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_seq = 0
        for j in range(len(s)):
            while s[j] in s[i:j]:
                i = i+1
            max_seq = max(max_seq, j+1-i)
        return max_seq
            