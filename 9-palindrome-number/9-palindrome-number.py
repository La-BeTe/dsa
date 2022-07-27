class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        old_x = x
        reversed_x = 0
        while x >= 1:
            reversed_x = (reversed_x * 10) + (x % 10)
            x //= 10
        return old_x == reversed_x