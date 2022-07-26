class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        result = 0
        while x >= 1:
            r = x % 10
            result = (result * 10) + r
            x = int(x / 10)
        limit = 2 ** 31
        if result < -limit or result > limit - 1:
            return 0
        return -result if is_negative else result
        