class Solution:
    def myAtoi(self, s: str) -> int:
        sign = None
        num = '0'
        num_map = {
            '0': 1,
            '1': 1,
            '2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 1,
            '8': 1,
            '9': 1
        }
        for char in s:
            if sign is None:
                if char == '-':
                    sign = -1
                elif char == '+':
                    sign = 1
                elif char in num_map:
                    sign = 1
                    num = char
                elif char != ' ' and char not in num_map:
                    break
            elif char in num_map:
                num += char
            elif char not in num_map:
                break
        limit = 2 ** 31 if sign and sign < 0 else (2 ** 31) - 1
        return min(limit, int(num)) * (sign or 1)