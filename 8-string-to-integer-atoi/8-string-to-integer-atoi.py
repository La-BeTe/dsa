class Solution:
    def myAtoi(self, s: str) -> int:
        sign = num = 0
        limit = (2 ** 31) - 1
        for char in s:
            is_num = ord(char) >= 48 and ord(char) <= 57
            if sign == 0:
                if char == '-':
                    sign = -1
                    limit += 1
                elif char == '+':
                    sign = 1
                elif char == ' ':
                    continue
                else:
                    sign = 1
                    if is_num:
                        num += int(char)
                    else:
                        break
            else:
                if is_num:
                    num = (num * 10) + int(char)
                else:
                    break
        return min(limit, num) * sign