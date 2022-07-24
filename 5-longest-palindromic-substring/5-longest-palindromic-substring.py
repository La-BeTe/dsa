class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        hash_map = {}
        for i, char in enumerate(s):
            hash_map[char] = [] if char not in hash_map else hash_map[char]
            hash_map[char].append(i)
        start, hash_map_ptr = 0, -1
        end, longest_palindrome, longest_palindrome_len = hash_map[s[start]][hash_map_ptr], '', 0
        while start < s_len:
            if longest_palindrome_len > (s_len - start):
                break
            end += 1
            can_move_start = False
            should_break = False
            if s[start] in hash_map and ((hash_map[s[start]][-1] - hash_map[s[start]][0]) < longest_palindrome_len):
                del hash_map[s[start]]
                can_move_start = True
            elif s[start] not in hash_map or (len(hash_map[s[start]]) + hash_map_ptr) < 0:
                can_move_start = True
            else:
                sliced_s = s[start:end]
                reversed_s = sliced_s[::-1]
                if sliced_s == reversed_s:
                    can_move_start = True
                    if len(reversed_s) > longest_palindrome_len:
                        longest_palindrome = reversed_s
                        longest_palindrome_len = len(reversed_s)
            if can_move_start:
                hash_map_ptr = 0
                while True:
                    start += 1
                    if start >= s_len:
                        should_break = True
                        break
                    if s[start] in hash_map:
                        break
            if should_break:
                break
            hash_map_ptr -= 1
            end = hash_map[s[start]][hash_map_ptr]
        return longest_palindrome
                