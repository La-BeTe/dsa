class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        result = 0
        abs_x = abs(x)
        limit = 2 ** 31
        while abs_x >= 1:
            result = (result * 10) + (abs_x % 10)
            if result > limit:
                return 0
            abs_x = abs_x // 10
        return result * x // abs(x)
        