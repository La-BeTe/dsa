class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, len(s)
        longest_palindrome = ''
        while start < len(s):
            if s[start] != s[end-1]:
                end -= 1
                continue
            if (end - start) < len(longest_palindrome):
                start += 1
                end = len(s)
                continue
            sliced_s = s[start:end]
            reversed_s = sliced_s[::-1]
            if sliced_s == reversed_s and len(reversed_s) > len(longest_palindrome):
                longest_palindrome = reversed_s
            end -= 1
        return longest_palindrome
                