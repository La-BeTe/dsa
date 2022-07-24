class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        start, end = 0, s_len
        longest_palindrome = ''
        longest_palindrome_len = 0
        while start < s_len:
            if longest_palindrome_len > (s_len - start):
                break
            if s[start] != s[end-1]:
                end -= 1
                continue
            if (end - start) < longest_palindrome_len:
                start += 1
                end = s_len
                continue
            sliced_s = s[start:end]
            reversed_s = sliced_s[::-1]
            if sliced_s == reversed_s:
                longest_palindrome = reversed_s
                longest_palindrome_len = len(reversed_s)
            end -= 1
        return longest_palindrome
                