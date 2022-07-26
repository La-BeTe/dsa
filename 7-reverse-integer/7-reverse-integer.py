class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        is_negative = -1 if x < 0 else 1
        x = abs(x)
        while x >= 1:
            r = x % 10
            result = (result * 10) + r
            x = x // 10
        return result * is_negative if result < 2 ** 31 else 0
        