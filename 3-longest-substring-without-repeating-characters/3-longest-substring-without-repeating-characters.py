class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left = 0
        # right = 0
        # longest_substr_length = 0
        # hash_map = {}
        # while True:
        #     if right >= len(s):
        #         longest_substr_length = max(longest_substr_length, right - left)
        #         break
        #     char = s[right]
        #     if char not in hash_map:
        #         hash_map[char] = right
        #         right += 1
        #     else:
        #         longest_substr_length = max(longest_substr_length, right - left)
        #         left = hash_map[char] + 1
        #         right = left
        #         hash_map = {}
        # return longest_substr_length
        left = 0
        longest_substr_length = -inf

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
        return longest_substr_length if longest_substr_length != -inf else 0
            