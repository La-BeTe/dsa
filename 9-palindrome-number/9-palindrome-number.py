class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        actual_x, reversed_x = x, 0
        while actual_x >= 1:
            reversed_x = (reversed_x * 10) + (actual_x % 10)
            actual_x //= 10
        return x == reversed_x