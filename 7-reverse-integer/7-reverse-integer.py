class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        abs_x = abs(x) or 1 # if x is 0, use 1 so we don't get ZeroDivisionError
        is_negative = x // abs_x
        while abs_x >= 1:
            result = (result * 10) + (abs_x % 10)
            abs_x = abs_x // 10
        return result * is_negative if result < 2 ** 31 else 0
        